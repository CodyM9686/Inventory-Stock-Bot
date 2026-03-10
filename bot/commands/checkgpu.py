'''
    Purpose: A discord bot command to pull currently available GPUs

'''


from discord.ext import commands
from tabulate import tabulate
import asyncio

# Track running tasks per user
running_tasks = {}

def chunk_string(string, chunk_size=1900):
    """Split string into chunks to avoid Discord message limit"""
    return [string[i:i+chunk_size] for i in range(0, len(string), chunk_size)]

@commands.command()
async def checkgpu(ctx):
    """Wrapper to call NeweggMonitor and send results in Discord."""
    from monitors.newegg_monitor import NeweggMonitor 

    monitor = NeweggMonitor()
    task = asyncio.create_task(_checkgpu_task(ctx, monitor))
    running_tasks[ctx.author.id] = task

async def _checkgpu_task(ctx, monitor):
    """Internal task that handles scraping and chunked message sending."""
    try:
        stock_data = monitor.get_products() 

        if isinstance(stock_data, str):
            await ctx.send(stock_data)
            return

        import pandas as pd
        df = pd.DataFrame(stock_data)

        # Optional: Only in-stock items
        in_stock_df = df[df['Availability'] == 'IN STOCK']
        if in_stock_df.empty:
            await ctx.send("No items currently in stock.")
            return

        table_string = tabulate(in_stock_df, headers='keys', tablefmt='grid', showindex=False)

        # Send table in chunks
        for chunk in chunk_string(table_string):
            # If user cancelled, stop sending
            if ctx.author.id not in running_tasks:
                await ctx.send("Task stopped.")
                return
            await ctx.send(f"```{chunk}```")
            await asyncio.sleep(1)

    except Exception as e:
        await ctx.send(f"Error while scraping: {e}")
    finally:
        running_tasks.pop(ctx.author.id, None)
        
# stop command
@commands.command()
async def stop(ctx):
    """Stop your current GPU scraping task."""
    task = running_tasks.pop(ctx.author.id, None)
    if task:
        task.cancel()
        await ctx.send("Stopped your current GPU check.")
    else:
        await ctx.send("No running task to stop.")