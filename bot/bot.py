'''
    Purpose: Store core functionality of the Disocrd bot

    To-Do:
        - Create more error handling and provide a temporary "turn off" feature. 

'''
from dotenv import load_dotenv
import os

load_dotenv()


import discord
from discord.ext import commands
from bot.commands.checkgpu import checkgpu, stop


TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()  
intents.message_content = True       


bot = commands.Bot(command_prefix="!", intents=intents)

# Event runs when bot connects
@bot.event
async def on_ready():
    print(f"Bot connected as {bot.user}")


bot.add_command(checkgpu)
bot.add_command(stop)

# Start the bot
bot.run(TOKEN)