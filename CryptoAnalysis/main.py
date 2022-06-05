import pandas as pd
from sqlalchemy.engine import URL
from sqlalchemy import create_engine

from Config import engine
from ProcessData import *
from Analysis import *



pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
desired_width = 300
pd.set_option('display.width', desired_width)



if __name__ == '__main__':

    a = "'Bitcoin'"
    df = read_time_sequence("Bitcoin")
    create_column_amountToken(df)
    print(df.head(10).to_string())
    print(df.info())

    '''
    graph_timesequences(df, ['Open'])
    graph_interval_timesequences(df, ['Open'], '2020-01-01', '2021-12-30')

    graph_timesequences(df, ['Open', 'High'])
    graph_interval_timesequences(df, ['Open', 'High'], '2020-01-01', '2021-12-30')

    df2 = read_time_sequence("Litecoin")
    create_column_amountToken(df2)
    print(df2.head(10).to_string())
    print(df2.info())
    graph_timesequence_cryptos([df, df2], 'Open')
    graph_interval_timesequence_cryptos([df, df2], 'Open', '2020-01-01', '2021-12-30')

    correlation_matrix(df2)
    '''

    '''
    decompose(df, 'High')
    decompose_interval(df, 'High', '2020-01-01', '2021-12-30')
    
    dickey_fuller_test(df, 'High')


    autocorr_partautocorr(df, 'High')
    '''
