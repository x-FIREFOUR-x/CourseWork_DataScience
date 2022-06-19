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


def analysis_forcast():

        #read all name tokens in df
    name_tokens = read_names_tokens()
    print(name_tokens.head(50))


        #read index token and input df name token
    index_token = int(input('\n -Input index: '))
    token = name_tokens.loc[index_token]['Name']


        #read df(data) input token
    df = read_time_sequence(token)
    create_column_amount(df)
    create_column_price(df)
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
    decompose(df, column)
    autocorr_partautocorr(df, column)

    #wavelet_smoothing_plot(df, column, 5)
    fft_smoothing_plot(df, column)
    filtred =move_average_plot(df, column, 10)


    train_day = int(input('\n -Введіть кількість днів для тренувальної послідовності: '))
    test_day = int(input(' -Введіть кількість днів для тестувальної послідовності: '))
    forecast_day = int(input(' -Введіть кількість днів на яку буде зроблено прогноз: '))

    AR(df, column, train_day, test_day, forecast_day)
    ARIMA(df, column, train_day, test_day, forecast_day)
    SARIMA(df, column, train_day, test_day, forecast_day)
    Holt_Winter(df, column, train_day, test_day, forecast_day)
    SES(df, column, train_day, test_day, forecast_day)


def show_tokens():
    name_tokens = read_names_prise_tokens()
    print(name_tokens.head(50))

    str_indexs = input("Введіть індекси токенів через пробіл: ")

    dfs = []
    if(str_indexs == ''):
        for i in range(0, name_tokens.shape[0]):
            df = read_time_sequence(name_tokens.loc[i]['Name'])
            create_column_amount(df)
            create_column_price(df)
            dfs.append(df)
    else:
        strs_indexs = str_indexs.split(sep=' ')

        indexs = []
        for str in strs_indexs:
            indexs.append(int(str))

        for i in indexs:
            df = read_time_sequence(name_tokens.loc[i]['Name'])
            create_column_amount(df)
            create_column_price(df)
            dfs.append(df)


    column = input('Введіть колонку: ')
    graph_timesequence_cryptos(dfs, column)

def console_interface():
    process = True
    while process:
        modul = input('Введіть: 1 -візуалізація токенів, 2 -аналіз і прогноз, інше -вихід: ')
        if modul == '1':
            show_tokens()
        else:
            if modul == '2':
                analysis_forcast()
            else:
                process = False


if __name__ == '__main__':
    console_interface()

