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


def console_interface():

        #read all name tokens in df
    name_tokens = read_names_tokens()
    print(name_tokens.head(50))


        #read index token and input df name token
    index_token = int(input('\n -Input index: '))
    token = name_tokens.loc[index_token]['Name']


        #read df(data) input token
    df = read_time_sequence(token)
    create_column_amountToken(df)
    create_column_Prise(df)
    print(df.head(10).to_string())
    #print(df.info())


        #read columns for graphics and matrix correlation
    str_columns = input('\n -Введіть колонки через пробіл: ')
    if (str_columns == ''):
        #str_columns = 'High Low Open Close Volume Marketcap amountToken'
        str_columns = 'High Low Open Close'
    columns = str_columns.split(sep=' ')

    correlation_matrix(df)
    graph_timesequences(df, columns)


        # read column timeseries which analysis and forcast
    column = input('\n -Введіть колонку, яку будем аналізувати і прогнозувати: ')

    dickey_fuller_test(df, column)
    autocorr_partautocorr(df, column)

    wavelet_smoothing_plot(df, column, 5)
    fft_smoothing_plot(df, column)
    move_average_plot(df, column, 10)


    train_day = int(input('\n -Введіть кількість днів для тренувальної послідовності: '))
    test_day = int(input(' -Введіть кількість днів для тестувальної послідовності: '))
    forecast_day = int(input(' -Введіть кількість днів на яку буде зроблено прогноз: '))

    print()
    AR(df, 'Low', train_day, test_day, forecast_day)
    ARIMA(df, 'Low', train_day, test_day, forecast_day)
    SARIMA(df, 'Low', train_day, test_day, forecast_day)
    Holt_Winter(df, 'Low', train_day, test_day, forecast_day)
    SES(df, 'Low', train_day, test_day, forecast_day)


def show_tokens():
    name_tokens = read_names_prise_tokens()
    print(name_tokens.head(50))

    str_indexs = input("Введіть індекси токенів через пробіл: ")

    dfs = []
    if(str_indexs == ''):
        for i in range(0, name_tokens.shape[0]):
            df = read_time_sequence(name_tokens.loc[i]['Name'])
            create_column_amountToken(df)
            create_column_Prise(df)
            dfs.append(df)
    else:
        strs_indexs = str_indexs.split(sep=' ')

        indexs = []
        for str in strs_indexs:
            indexs.append(int(str))

        for i in indexs:
            df = read_time_sequence(name_tokens.loc[i]['Name'])
            create_column_amountToken(df)
            create_column_Prise(df)
            dfs.append(df)


    column = input('Введіть колонку: ')
    graph_timesequence_cryptos(dfs, column)


if __name__ == '__main__':

    #console_interface()
    show_tokens()

    '''
    a = "Bitcoin"
    #a = "Aave"
    df = read_time_sequence(a)
    create_column_amountToken(df)
    print(df.head(10).to_string())
    print(df.info())


    #ARIMA(df, 'Low')
    #ARIMA(df, 'Low', 70, 20, 20)

    #SARIMA(df, 'Low')
    #SARIMA(df, 'Low', 70, 20, 20)

    #Holt_Winter(df, 'Low')
    #Holt_Winter(df, 'Low', 70, 25, 20)

    # SES(df, 'Low')
    #SES(df, 'Low', 70, 25, 20)
    #AR(df, 'Low', 100, 25, 20)
    '''


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

