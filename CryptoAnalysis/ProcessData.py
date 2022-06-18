import pandas as pd

from Config import engine

def read_time_sequence(name_crypto):
    query = "SELECT * FROM Cryptocurrency WHERE Name = '" + name_crypto + "' ORDER BY Name"
    df = pd.read_sql(query, engine, index_col=['Date'], parse_dates=['Date'])
    return df

def read_names_tokens():
    query = "SELECT [Name] FROM Cryptocurrency GROUP BY [Name] ORDER BY Name"
    name_tokens = pd.read_sql(query, engine)
    return name_tokens


def read_names_prise_tokens():
    query = "SELECT [Name], Max([Low]) AS [Prise] FROM Cryptocurrency GROUP BY [Name] ORDER BY [Prise]"
    name_tokens = pd.read_sql(query, engine)
    return name_tokens


def create_column_amountToken(df):
    df['amountToken'] = df['Marketcap'] / df['Close']


def create_column_Prise(df):
    df['Prise'] = (df['High'] + df['Low'])/2


