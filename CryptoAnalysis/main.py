import pandas as pd
from sqlalchemy.engine import URL
from sqlalchemy import create_engine

from Config import engine

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def read_time_sequence(name_crypto):
    query = "SELECT * FROM Cryptocurrency WHERE Name = '" + name_crypto + "' ORDER BY Name"
    df = pd.read_sql(query, engine, index_col=['Date'], parse_dates=['Date'])
    return df

if __name__ == '__main__':

    a = "'Bitcoin'"
    df = read_time_sequence("Bitcoin")
    print(df.head(10).to_string())
    print(df.info())

