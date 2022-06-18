from statsmodels.tsa.api import Holt
import matplotlib.pyplot as plt

import numpy as np
from itertools import product

from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score

from Models import *



    #built model Holt-Winter
def Holt_Winter(df, column, len_train=0, len_test=0, len_forcast=50 ):
    """model Holt-Winter's
            df - dataframe timeseries
            column - name column with timeserias in dataframe
            len_train - number day train data
            len_test - number day test data
            len_forcast - number day predict in the future
    """

    sl = np.arange(0, 1, 0.1)
    st = np.arange(0, 1, 0.1)
    parameters = product(sl, st)
    parameters_list = list(parameters)

    # split dataframe to train and test dataframe (timeseries)
    dfs, train_df, test_df, len_train, len_test = train_test_data(df, column, len_train, len_test)

    # select better model and build model
    best_model = optimize_holt(train_df, column, parameters_list)
    print(best_model.summary())

    # test metrics
    metrics(test_df[column], best_model)

    # build plot
    plot_holt(dfs[column], column, best_model, len_test, len_forcast)



    # select the best parameters model Holt-Winter
def optimize_holt(df, column, parameters_list):
    """Return the best model Holt-Winter corresponding AIC
            parameters_list - list with (sl, st) tuples
        """
    best_aic = float("inf")
    best_model = 0

    print("Selecting params for Holt-Winter's")
    print("aic                params")
    for param in parameters_list:
        # we need try-except because on some combinations model fails to converge
        try:
            model = Holt(df[column], initialization_method="estimated").fit(
                smoothing_level=param[0], smoothing_trend=param[1], optimized=False
            )
        except:
            continue
        aic = model.aic
        # saving best model, AIC and parameters
        if aic < best_aic:
            print(aic, param)
            best_model = model
            best_aic = aic
            best_param = param


    return best_model



    #build plot Holt-Winter
def plot_holt(series, column, model, len_test_data, len_forcast):
    """Plots model vs predicted values
        series - dataset with timeseries
        column - column timeserias in serias
        model - fitted ARIMA model
        len_test_data - number test data
        len_forcast - number of steps to predict in the future
    """

    #adding traing forcast
    forecast_train_data = model.fittedvalues

    #forecasting on test_data and n_steps forward
    forecast = forecast_train_data.append(model.forecast(len_test_data+len_forcast))

    #error = mean_absolute_percentage_error(data['actual'][s + d:], data['sarima_model'][s + d:])

    plt.figure(figsize=(15, 7))
    #plt.title("Forkast model SARIMA, paramet: " + column + "\nMean Absolute Percentage Error: {0:.2f}%".format(error))
    plt.title("Forkast model HOLT, column: " + column)
    plt.plot(forecast, color='r', label="model")
    plt.axvspan(series.index[series.shape[0] - len_test_data - 1], forecast.index[-1], alpha=0.5, color='lightgrey')
    plt.plot(series, label="actual")
    plt.legend()
    plt.grid(True)
    plt.show()
