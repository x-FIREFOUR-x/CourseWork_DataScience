import pandas as pd
from sqlalchemy.engine import URL
from sqlalchemy import create_engine

from Config import engine
from ProcessData import *
from Analysis import *

from Arima import *
from Sarima import *
from HoltWinter import *
from Ses import *
from Autoregression import *





pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)
desired_width = 300
pd.set_option('display.width', desired_width)



if __name__ == '__main__':

    a = "Bitcoin"
    #a = "Aave"
    df = read_time_sequence(a)
    create_column_amountToken(df)
    print(df.head(10).to_string())
    print(df.info())


    #ARIMA(df, 'Low')
    #ARIMA(df, 'Low', 100, 25, 20)

    #SARIMA(df, 'Low')
    #SARIMA(df, 'Low', 50, 50, 20)

    #Holt_Winter(df, 'Low')
    #Holt_Winter(df, 'Low', 50, 25, 20)

    # SES(df, 'Low')
    #SES(df, 'Low', 80, 25, 20)
    AR(df, 'Low', 200, 25, 20)




    '''
    print(df.index[-1])

    #dickey_fuller_test(df, 'Open')
    autocorr_partautocorr(df, 'Open')
    #model_arima(df, 'Open', p=1, d=1, q=2)
    model_arima(df, 'Open', p=3, d=1, q=3)
    '''

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



    '''
    wavelet_smoothing_plot(df, 'Close', 5)
    wavelet_smoothing_with_interval_plot(df, 'Close', 5, '2020-01-01', '2021-12-30')
    
    fft_smoothing_plot(df, 'Close')
    fft_smoothing_with_interval_plot(df, 'Close', '2020-01-01', '2021-12-30')
    
    move_average_plot(df, 'Close', 10)
    move_average_with_interval_plot(df, 'Close', 10, '2020-01-01', '2021-12-30')
    '''

