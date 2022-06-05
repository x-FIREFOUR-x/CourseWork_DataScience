import pandas as pd

from Config import engine

def read_time_sequence(name_crypto):
    query = "SELECT * FROM Cryptocurrency WHERE Name = '" + name_crypto + "' ORDER BY Name"
    df = pd.read_sql(query, engine, index_col=['Date'], parse_dates=['Date'])
    return df

def create_column_amountToken(df):
    df['amountToken'] = df['Marketcap'] / df['Close']