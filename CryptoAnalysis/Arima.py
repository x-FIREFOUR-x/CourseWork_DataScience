import warnings                                  # do not disturbe mode
warnings.filterwarnings('ignore')

import pandas as pd                              # tables and data manipulations
import matplotlib.pyplot as plt                  # plots

import statsmodels.api as sm

from itertools import product                    # some useful functions

from Analysis import *
from Models import *


def model_arima(df, column, p, d, q):
    train_data = df[column].loc[df.index[0:]]
    print(train_data.head(10))
    train_data.describe()
    print(train_data.head())

    '''
    d = 0
    if(dickey_fuller_test(df, column)):
        d = 0
    else:
        d = 1
    '''

    #model = smt.ARIMA(train_data, order=(1, 0, 1)).fit()
    model = smt.ARIMA(train_data, order=(p, d, q)).fit()
    model.summary()
    print(model.summary())

    fig, ax = plt.subplots(figsize=(15, 10))
    fig.suptitle('Прогноз', fontsize=16)
    ax = train_data.loc[train_data.index[-365:]].plot()
    ax.vlines(train_data.index[-1], 0, 1.5, linestyle='-', color='r')
    model.predict(train_data.index[-365], df.index[-1], dynamic=True, plot_insample=False, ax=ax).plot()
    plt.show()



def ARIMA(df, column):
    ps = range(2, 5)
    d = 1
    qs = range(2, 5)

    # creating list with all the possible combinations of parameters
    parameters = product(ps, qs)
    parameters_list = list(parameters)
    len(parameters_list)

    # split dataframe to train and test dataframe (timeseries)
    len_test = 20
    len_train = 255
    dfs, train_df, test_df, len_train, len_test = train_test_data(df, column, len_train, len_test)

    # select better parameters model
    result_table = optimizeARIMA(train_df, column, parameters_list, d)
    p, q = result_table.parameters[0]

    # build best model
    #best_model = sm.tsa.statespace.ARIMAX(train_df[column], order=(p, d, q)).fit()
    best_model = smt.ARIMA(train_df[column], order=(p, d, q)).fit()
    print(best_model.summary())

    # build plot
    plotARIMA(df[column], column, best_model, len_test, 50)

    '''
    len_test = 20
    len_train = 255
    dfs, train_df, test_df, len_train, len_test = train_test_data(df, column, len_train, len_test)

    #best_model = sm.tsa.statespace.ARIMAX(train_df[column], order=(4, d, 4)).fit(disp=-1)
    best_model = smt.ARIMA(train_df[column], order=(4, d, 4)).fit()
    plotSARIMA(dfs[column], column, best_model, len_test, 50, s, d)
    '''



def optimizeARIMA(df, column, parameters_list, d):
    """Return dataframe with parameters and corresponding AIC
        parameters_list - list with (p, q) tuples
        d - integration order in ARIMA model
    """

    results = []
    best_aic = float("inf")

    for param in parameters_list:
        # we need try-except because on some combinations model fails to converge
        try:
            model = smt.ARIMA(df[column], order=(param[0], d, param[1])).fit()
            #model = sm.tsa.statespace.ARIMAX(df[column], order=(param[0], d, param[1])).fit(disp=-1)
        except:
            continue
        aic = model.aic
        # saving best model, AIC and parameters
        if aic < best_aic:
            best_model = model
            best_aic = aic
            best_param = param

        if(model.aic > 500):
            print(param, model.aic)
            results.append([param, model.aic])

    result_table = pd.DataFrame(results)
    result_table.columns = ['parameters', 'aic']

    # sorting in ascending order, the lower AIC is - the better
    result_table = result_table.sort_values(by='aic', ascending=True).reset_index(drop=True)

    return result_table


def plotARIMA(series, column, model, len_test_data, len_forcast):
    """Plots model vs predicted values
        series - dataset with timeseries
        column - column timeserias in serias
        model - fitted ARIMA model
        len_test_data - number test data
        len_forcast - number of steps to predict in the future
    """

    #adding serias
    data = series.copy()
    data = pd.DataFrame(list(data), columns=['actual'], index=data.index)

    #adding serias models train_data
    data['arima_model'] = model.fittedvalues

    # forecasting on test_data and n_steps forward
    forecast = model.predict(start=data.shape[0] - len_test_data, end=data.shape[0] + len_forcast)
    forecast = data.arima_model.append(forecast)

    #error = mean_absolute_percentage_error(data['actual'][s + d:], data['sarima_model'][s + d:])

    plt.figure(figsize=(15, 7))
    #plt.title("Forkast model SARIMA, paramet: " + column + "\nMean Absolute Percentage Error: {0:.2f}%".format(error))
    plt.title("Forkast model ARIMA, column: " + column)
    plt.plot(forecast, color='r', label="model")
    plt.axvspan(data.index[data.shape[0] - len_test_data - 1], forecast.index[-1], alpha=0.5, color='lightgrey')
    plt.plot(data.actual, label="actual")
    plt.legend()
    plt.grid(True)
    plt.show()

