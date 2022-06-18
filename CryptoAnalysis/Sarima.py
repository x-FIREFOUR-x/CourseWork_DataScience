import warnings                                  # do not disturbe mode
warnings.filterwarnings('ignore')

import pandas as pd                              # tables and data manipulations
import matplotlib.pyplot as plt                  # plots

import statsmodels.api as sm

from itertools import product                    # some useful functions

from sklearn.metrics import r2_score, median_absolute_error, mean_absolute_error, mean_absolute_percentage_error
from sklearn.metrics import median_absolute_error, mean_squared_error, mean_squared_log_error

from Models import *



    #model SARIMA
def SARIMA(df, column, len_train=0, len_test=0, len_forcast=50):
    """model SARIMA
            df - dataframe timeseries
            column - name column with timeserias in dataframe
            len_train - number day train data
            len_test - number day test data
            len_forcast - number day predict in the future
    """

    ps = range(2, 5)
    d = 1
    qs = range(2, 5)
    Ps = range(0, 2)
    D = 1
    Qs = range(0, 2)
    s = 24  # season length is still 24

    # creating list with all the possible combinations of parameters
    parameters = product(ps, qs, Ps, Qs)
    parameters_list = list(parameters)
    len(parameters_list)

    # split dataframe to train and test dataframe (timeseries)
    dfs, train_df, test_df, len_train, len_test = train_test_data(df, column, len_train, len_test)

    # select better model and build
    best_model = optimizeSARIMA(train_df, test_df, column, parameters_list, d, D, s)
    print(best_model.summary())

    # test metrics
    metrics(test_df[column], best_model)

    # build plot
    plotSARIMA(dfs[column], column, best_model, len_test, len_forcast)



    #select the best model SARIMA
def optimizeSARIMA(df, test, column, parameters_list, d, D, s):
    """Return the best model SARIMA and corresponding AIC
        parameters_list - list with (p, q, P, Q) tuples
        d - integration order in ARIMA model
        D - seasonal integration order
        s - length of season
    """

    results = []
    best_mape = float("inf")

    print("Selecting params for SARIMA")
    print("params       mape")
    for param in parameters_list:
        # we need try-except because on some combinations model fails to converge
        try:
            model = sm.tsa.statespace.SARIMAX(df[column],
                                              order=(param[0], d, param[1]),
                                              seasonal_order=(param[2], D, param[3], s)
                                              ).fit(disp=-1)
        except:
            continue

        mape = mean_absolute_percentage_error(test[column], model.predict(start=test.index[0], end=test.index[-1]))
        print(param, mape)

        # saving best model, AIC and parameters
        if (mape < best_mape ):
            best_model = model
            best_mape = mape
            best_param = param
            results.append([param, mape])

    result_table = pd.DataFrame(results)
    result_table.columns = ['parameters', 'aic']


    return best_model



    #build plot SARIMA
def plotSARIMA(series, column, model, len_test_data, len_forcast):
    """Plots model vs predicted values
        series - dataset with timeseries
        column - column timeserias in serias
        model - fitted SARIMA model
        len_test_data - number test data
        len_forcast - number of steps to predict in the future
    """

    #adding serias
    data = series.copy()
    data = pd.DataFrame(list(data), columns=['actual'], index=data.index)

    #adding serias models train_data
    data['sarima_model'] = model.fittedvalues

    # forecasting on test_data and n_steps forward
    forecast = model.predict(start=data.shape[0] - len_test_data - 1, end=data.shape[0] + len_forcast)
    forecast = data.sarima_model.append(forecast)

    #error = mean_absolute_percentage_error(data['actual'][s + d:], data['sarima_model'][s + d:])

    plt.figure(figsize=(12, 6))
    plt.title("Forkast model SARIMA, column: " + column)
    plt.plot(forecast, color='r', label="model")
    plt.axvspan(data.index[data.shape[0] - len_test_data - 1], forecast.index[-1], alpha=0.5, color='lightgrey')
    plt.plot(data.actual, label="actual")
    plt.legend()
    plt.grid(True)
    plt.show()




