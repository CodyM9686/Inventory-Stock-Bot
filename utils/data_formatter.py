import pandas as pd
from tabulate import tabulate

'''
Purpose: Utility for creating pandas dataframe to display data. 

'''

def create_dataframe(stock_data):

    if isinstance(stock_data, str):
        return stock_data

    df = pd.DataFrame(stock_data)

    table = tabulate(
        df,
        headers='keys',
        tablefmt='grid',
        showindex=False
    )

    return table