import matplotlib.pyplot as plt
import statsmodels.tsa.api as smt
import pandas as pd
import numpy as np
from statsmodels.graphics.tsaplots import plot_acf, plot_pacf
from scipy import signal
import pywt



    #побудувати графік числових послідовностей значень масиву name_columns криптовалюти df(dataframe)
def graph_timesequences(df, name_columns):
    index = df.index[0]
    title = 'Часова динаміка величин: '
    for name in name_columns:
        title = title + name + ', '
    title = title + ' криптовалюти ' + df.loc[index]['Name']

    fig, ax = plt.subplots(figsize=(12, 6))
    for name in name_columns:
        df[name].plot(ax=ax)
    plt.title(title)
    ax.grid()
    ax.legend()
    plt.show()


    #впобудувати графік числових послідовностей значень масиву name_columns криптовалюти df(dataframe)
        #за інтервал часу [start_date; end_date]
def graph_interval_timesequences(df, name_columns, start_date, end_date):
    index = df.index[0]
    title = 'Часова динаміка величин: '
    for name in name_columns:
        title = title + name + ', '
    title = title + ' криптовалюти ' + df.loc[index]['Name']+\
            ' з ' + start_date + ' по ' + end_date

    fig, ax = plt.subplots(figsize=(12, 6))
    for name in name_columns:
        df[[name]].loc[start_date + ' 00:00:00' : end_date + ' 00:00:00'].plot(ax=ax)
    plt.title(title)
    ax.grid()
    ax.legend()
    plt.show()


    #побудувати графік числових послідовностей значення name_column криптовалют dfs(масив dataframes)
def graph_timesequence_cryptos(dfs, name_column):
    title = 'Часова динаміка величини ' + name_column + '\n криптовалют: '
    for df in dfs:
        title = title + df.loc[df.index[0]]['Name'] + ', '

    fig, ax = plt.subplots(figsize=(12, 6))
    linelegend = []
    for df in dfs:
        df[name_column].plot(ax=ax)
        linelegend.append(df.loc[df.index[0]]['Name'])

    plt.title(title)
    ax.grid()
    ax.legend(linelegend)
    plt.show()


    #побудувати графік числових послідовностей значення name_column криптовалют dfs(масив dataframes)
    # за інтервал часу [start_date; end_date]
def graph_interval_timesequence_cryptos(dfs, name_column, start_date, end_date):
    title = 'Часова динаміка величини ' + name_column + ' з ' + start_date + ' по ' + end_date + '\n криптовалют: '
    for df in dfs:
        title = title + df.loc[df.index[0]]['Name'] + ', '

    fig, ax = plt.subplots(figsize=(12, 6))
    linelegend = []
    for df in dfs:
        df[name_column].loc[start_date + ' 00:00:00' : end_date + ' 00:00:00'].plot(ax=ax)
        linelegend.append(df.loc[df.index[0]]['Name'])

    plt.title(title)
    ax.grid()
    ax.legend(linelegend)
    plt.show()





    #матриця кореляції
def correlation_matrix(df):
    corr = df[['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap', 'Amount', 'Price']].corr()
    print("Matrix correlation " + df.loc[df.index[0]]['Name'])
    print(corr)





    # декомпозиція часового ряду на тренд, сезонність і домішки
def decompose(df, column):
    series = df[column]
    decomposition = smt.seasonal_decompose(series[~series.isna()])
    fig = decomposition.plot()
    fig.set_size_inches(12, 6)
    title = 'Декомпозиція крипто валюти ' + df.loc[df.index[0]]['Name']
    fig.suptitle(title, fontsize=15)
    plt.show()


    #декомпозиція часового ряду на тренд, сезонність і домішки за проміжок часу [start_date; end_date]
def decompose_interval(df, column, start_date, end_date):
    series = df[column]
    decomposition = smt.seasonal_decompose(series.loc[start_date + ' 00:00:00' : end_date + ' 00:00:00'][~series.isna()])
    fig = decomposition.plot()
    fig.set_size_inches(12, 6)
    title = 'Декомпозиція крипто валюти ' + df.loc[df.index[0]]['Name']
    fig.suptitle(title, fontsize=15)
    plt.show()





    #тест Діккі-Фуллера на стаціонарність рядку
def dickey_fuller_test(df, column):
    series = df[column]
    test = smt.adfuller(series[~series.isna()], autolag='AIC')
    print('adf: ', test[0])
    print('p-value: ', test[1])
    print('Critical values: ', test[4])
    if test[0] > test[4]['5%']:
        print('Наявні одиничні корені, ряд не стаціонарний.')
        return False
    else:
        print('Одиничні корені відсутні, ряд є стаціонарним.')
        return True



    #аутокореляція і часткова автокореляція
def autocorr_partautocorr(df, column):
    series = df[column]
    fig, ax = plt.subplots(2, figsize=(12, 6))
    title = 'Автокореляція і часткова автокореляція ' + df.loc[df.index[0]]['Name'] + ' величини ' + column
    fig.suptitle(title, fontsize=15)
    ax[0] = plot_acf(series[~series.isna()], ax=ax[0], lags=120)
    ax[1] = plot_pacf(series[~series.isna()], ax=ax[1], lags=120)
    plt.show()





    #середнє квадратичне відхилення d
def madev(d):
    return np.mean(np.absolute(d - np.mean(d)))



    #згладжування методом Вейвлет
def wavelet_smoothing(x, level=1, wavelet='db4'):
    coeff = pywt.wavedec(x, wavelet, mode="per")
    sigma = (1/0.6745) * madev(coeff[-level])
    uthresh = sigma * np.sqrt(2 * np.log(len(x)))
    coeff[1:] = (pywt.threshold(i, value=uthresh, mode='hard') for i in coeff[1:])
    return pywt.waverec(coeff, wavelet, mode='per')


    #побудова графіка згладжуваних послідовностей методом Вейвлет
def wavelet_smoothing_plot(x, column, n):
    x = x[column]
    filtered = wavelet_smoothing(x, wavelet='bior3.1', level=n)
    plt.figure(figsize=(12, 6))
    plt.plot(x, label='Raw')
    filtered = filtered[:x.shape[0]]
    filtered_frame = pd.DataFrame(filtered, columns=[column], index = x.index)
    plt.plot(filtered_frame, label='Filtered')
    plt.legend()
    plt.title(f"DWT Denoising with {n} Wavelets, {column}", size=15)
    plt.show()

    return filtered_frame


    #побудова графіка згладжуваних послідовностей на інтервалі методом Вейвлет
def wavelet_smoothing_with_interval_plot(x, column, n, start_date, end_date):
    x = x[column].loc[start_date + ' 00:00:00': end_date + ' 00:00:00'][~x[column].isna()]
    filtered = wavelet_smoothing(x, wavelet='bior3.1', level=n)
    plt.figure(figsize=(12, 6))
    plt.plot(x, label='Raw')
    filtered = filtered[:x.shape[0]]
    filtered_frame = pd.DataFrame(filtered, columns=[column], index = x.index)
    plt.plot(filtered_frame, label='Filtered')
    plt.legend()
    plt.title(f"DWT Denoising with {n} Wavelets, {column}", size=15)
    plt.show()

    return filtered_frame




    #побудова графіка згладжуваних послідовностей методом Фур'є
def fft_smoothing_plot(x, column, sigma=40, m=1):
    x = x[column]
    win = np.roll(signal.general_gaussian(x.shape[0], m, sigma), x.shape[0] // 2)
    XX = np.hstack((x, np.flip(x)))
    fXX = np.fft.fft(XX, n = x.shape[0])
    XXf = np.real(np.fft.ifft(fXX * win))[:x.shape[0]]
    plt.figure(figsize=(12, 6))
    plt.plot(x, label='Raw')
    filtered_frame = pd.DataFrame(XXf, columns=[column], index=x.index)
    plt.plot(filtered_frame, label='Filtered')
    plt.legend()
    plt.title(f"FFT Denoising with sigma = {sigma} and m = {m}, {column}", size=15)
    plt.show()

    return filtered_frame


    #побудова графіка згладжуваних послідовностей на інтервалі методом Фур'є
def fft_smoothing_with_interval_plot(x, column, start_date, end_date, sigma=40, m=1):
    x = x[column].loc[start_date + ' 00:00:00': end_date + ' 00:00:00'][~x[column].isna()]
    win = np.roll(signal.general_gaussian(x.shape[0], m, sigma), x.shape[0] // 2)
    XX = np.hstack((x, np.flip(x)))
    fXX = np.fft.fft(XX, n = x.shape[0])
    XXf = np.real(np.fft.ifft(fXX * win))[:x.shape[0]]
    plt.figure(figsize=(12, 6))
    plt.plot(x, label='Raw')
    filtered_frame = pd.DataFrame(XXf, columns=[column], index=x.index)
    plt.plot(filtered_frame, label='Filtered')
    plt.legend()
    plt.title(f"FFT Denoising with sigma = {sigma} and m = {m}, {column}", size=15)
    plt.show()

    return filtered_frame




    #побудова графіка згладжуваних послідовностей методом ковзаючого середнього
def move_average_plot(x, column, n):
    x=x[column]
    rolling_mean = x.rolling(n).mean()
    rolling_mean = pd.DataFrame(rolling_mean, columns=[column], index=x.index)
    plt.figure(figsize=(12, 6))
    plt.plot(x, label='Raw')
    plt.plot(rolling_mean, label='Filtred')
    plt.legend(loc='upper left')
    plt.title(f'Rolling with n = {n}, {column}', size=15)
    plt.show()

    return rolling_mean


    #побудова графіка згладжуваних послідовностей на інтервалі методом ковзаючого середнього
def move_average_with_interval_plot(x, column, n, start_date, end_date):
    x=x[column].loc[start_date + ' 00:00:00': end_date + ' 00:00:00'][~x[column].isna()]
    rolling_mean = x.rolling(n).mean()
    rolling_mean = pd.DataFrame(rolling_mean, columns=[column], index=x.index)
    plt.figure(figsize=(12, 6))
    plt.plot(x, label='Raw')
    plt.plot(rolling_mean, label='Filtred')
    plt.legend(loc='upper left')
    plt.title(f'Rolling with n = {n}, {column}', size=15)
    plt.show()

    return rolling_mean

