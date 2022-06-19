import warnings
warnings.filterwarnings('ignore')

import pandas as pd
from statsmodels.tsa.ar_model import AutoReg

from Models import *


    #model AR
def AR(df, column, len_train=0, len_test=0, len_forcast=50):
    """model ARIMA
            df - dataframe timeseries
            column - name column with timeserias in dataframe
            len_train - number day train data
            len_test - number day test data
            len_forcast - number day predict in the future
    """

    lags = range(0, 100)
    #len_train = len_train + lags

    # split dataframe to train and test dataframe (timeseries)
    dfs, train_df, test_df, len_train, len_test = train_test_data(df, column, len_train, len_test)

    #select better model and build model
    best_model, lags = optimizeAR(train_df, column, lags, test_df)
    print(best_model.summary())

    # test metrics
    metrics(test_df[column], best_model)

    # build plot
    plotAR(dfs[column], column, best_model, len_test, len_forcast)
    qq_and_residual_plot(test_df[column], best_model)


    #select the best model AR
def optimizeAR(df, column, parameters_list, test):

    best_mape = float("inf")
    best_model = 0
    best_lags = 0

    print("Selecting params for AR")
    print("lags   mape")
    for lags in parameters_list:
        # we need try-except because on some combinations model fails to converge
        try:
            model = AutoReg(df[column], lags=lags).fit()
        except:
            continue

        mape = mean_absolute_percentage_error(test[column], model.predict(start=test.index[0], end=test.index[-1]))
        # saving best model, MAPE and parameters
        if mape < best_mape:
            best_model = model
            best_mape = mape
            best_lags = lags
            print(lags, "   ", mape)
    return (best_model, best_lags)



    #build plot AR
def plotAR(series, column, model, len_test_data, len_forcast):
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
    data['ar_model'] = model.fittedvalues

    # forecasting on test_data and n_steps forward
    forecast = model.predict(start=data.shape[0] - len_test_data - 1, end=data.shape[0] + len_forcast)
    forecast = data.ar_model.append(forecast)

    plt.figure(figsize=(12, 6))
    plt.title("Forecast model AR, column: " + column)
    plt.plot(forecast, color='r', label="model")
    plt.axvspan(data.index[data.shape[0] - len_test_data - 1], forecast.index[-1], alpha=0.5, color='lightgrey')
    plt.plot(data.actual, label="actual")
    plt.legend()
    plt.grid(True)
    plt.show()
