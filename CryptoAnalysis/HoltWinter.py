from statsmodels.tsa.api import Holt
import matplotlib.pyplot as plt
from Models import *
import numpy as np
from itertools import product

def Holt_Winter(df, column ):
    sl = np.arange(0, 1, 0.1)
    st = np.arange(0, 1, 0.1)
    parameters = product(sl, st)
    parameters_list = list(parameters)

    len_test = 20
    len_train = 250
    dfs, train_df, test_df, len_train, len_test = train_test_data(df, column, len_train, len_test)

    best_model = optimize_holt(train_df, column, parameters_list)
    print(best_model)


    # build plot
    plot_holt(df, column, best_model, len_test, 50)

def optimize_holt(df, column, parameters_list):
    best_aic = float("inf")
    best_model = 0

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
            print("AIC: ", aic)
            best_model = model
            best_aic = aic
            best_param = param

    # sorting in ascending order, the lower AIC is - the bette

    return best_model
'''fit1 = Holt(data[column], initialization_method="estimated").fit(
        smoothing_level=0.8, smoothing_trend=0.2, optimized=False
    )
    fcast1 = fit1.forecast(10).rename("Holt's linear trend")
    plt.figure(figsize=(12, 8))
    plt.plot(data[column], marker="o", color="black")
    plt.plot(fit1.fittedvalues, color="blue")
    (line1,) = plt.plot(fcast1, marker="o", color="blue")
    plt.legend([line1], [fcast1.name])
    plt.show()'''

def plot_holt(df, column, model, len_test_data, len_forcast):
    """Plots model vs predicted values
        series - dataset with timeseries
        column - column timeserias in serias
        model - fitted ARIMA model
        len_test_data - number test data
        len_forcast - number of steps to predict in the future
    """

    #adding serias


    # forecasting on test_data and n_steps forward
    forecast = model.fittedvalues.append(model.forecast(len_forcast))

    #error = mean_absolute_percentage_error(data['actual'][s + d:], data['sarima_model'][s + d:])

    plt.figure(figsize=(15, 7))
    #plt.title("Forkast model SARIMA, paramet: " + column + "\nMean Absolute Percentage Error: {0:.2f}%".format(error))
    plt.title("Forkast model HOLT, column: " + column)
    plt.plot(forecast, color='r', label="model")
    plt.axvspan(df.index[df.shape[0] - len_test_data - 1], forecast.index[-1], alpha=0.5, color='lightgrey')
    plt.plot(df[column], label="actual")
    print(df[column])
    plt.legend()
    plt.grid(True)
    plt.show()