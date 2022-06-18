import warnings                                  # do not disturbe mode
warnings.filterwarnings('ignore')

import pandas as pd                              # tables and data manipulations
import matplotlib.pyplot as plt                  # plots

from itertools import product                    # some useful functions

import statsmodels.tsa.api as smt

from Models import *


    #model ARIMA
def ARIMA(df, column, len_train=0, len_test=0, len_forcast=50):
    """model ARIMA
            df - dataframe timeseries
            column - name column with timeserias in dataframe
            len_train - number day train data
            len_test - number day test data
            len_forcast - number day predict in the future
    """

    ps = range(2, 5)
    ds = range(0, 5)
    qs = range(2, 5)

    # creating list with all the possible combinations of parameters
    parameters = product(ps, ds, qs)
    parameters_list = list(parameters)
    len(parameters_list)

    # split dataframe to train and test dataframe (timeseries)
    dfs, train_df, test_df, len_train, len_test = train_test_data(df, column, len_train, len_test)

    #select better model and build model
    best_model = optimizeARIMA(train_df, test_df, column, parameters_list)
    print(best_model.summary())

    # test metrics
    metrics(test_df[column], best_model)

    # build plot
    plotARIMA(dfs[column], column, best_model, len_test, len_forcast)



    #select the best model ARIMA
def optimizeARIMA(df, test, column, parameters_list):
    """Return the best model ARIMA corresponding AIC
        parameters_list - list with (p, d, q) tuples
    """

    results = []
    best_mape = float("inf")

    print("Selecting params for ARIMA")
    print("params    mape")

    for param in parameters_list:
        # we need try-except because on some combinations model fails to converge
        try:
            model = smt.ARIMA(df[column], order=(param[0], param[1], param[2])).fit()
        except:
            continue

        mape = mean_absolute_percentage_error(test[column], model.predict(start=test.index[0], end=test.index[-1]))
        print(param, mape)
        #plotARIMA(dfs, column, model, len_test, len_forcast)

        # saving best model, AIC and parameters
        if (mape < best_mape and mape > 0.1):
            best_model = model
            best_mape = mape
            best_param = param
            results.append([param, mape])

    return best_model



    #build plot ARIMA
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
    forecast = model.predict(start=data.shape[0] - len_test_data - 1, end=data.shape[0] + len_forcast)
    forecast = data.arima_model.append(forecast)

    #error = mean_absolute_percentage_error(data['actual'][s + d:], data['sarima_model'][s + d:])

    plt.figure(figsize=(12, 6))
    #plt.title("Forkast model SARIMA, paramet: " + column + "\nMean Absolute Percentage Error: {0:.2f}%".format(error))
    plt.title("Forkast model ARIMA, column: " + column)
    plt.plot(forecast, color='r', label="model")
    plt.axvspan(data.index[data.shape[0] - len_test_data - 1], forecast.index[-1], alpha=0.5, color='lightgrey')
    plt.plot(data.actual, label="actual")
    plt.legend()
    plt.grid(True)
    plt.show()

