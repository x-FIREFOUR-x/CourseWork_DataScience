import pandas as pd
from sqlalchemy.engine import URL
from sqlalchemy import create_engine

from Config import engine
from ProcessData import *


if __name__ == '__main__':

    a = "'Bitcoin'"
    df = read_time_sequence("Bitcoin")
    create_column_amountToken(df)
    print(df.head(10).to_string())
    print(df.info())

