import warnings                                  # do not disturbe mode
warnings.filterwarnings('ignore')

import pandas as pd                              # tables and data manipulations
import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error  # plots

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

    lags = 35

    # creating list with all the possible combinations of parameters

    # split dataframe to train and test dataframe (timeseries)
    dfs, train_df, test_df, len_train, len_test = train_test_data(df, column, len_train, len_test)

    #select better model and build model
    best_model = optimizeAR(train_df, column, lags)
    print(best_model.summary())

    # test metrics
    metrics(test_df[column], best_model)

    # build plot
    plotAR(dfs[column], column, best_model, len_test, len_forcast)



    #select the best model AR
def optimizeAR(df, column, lags):
    return AutoReg(df[column], lags=lags).fit()



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

    plt.figure(figsize=(15, 7))
    plt.title("Forecast model AR, column: " + column)
    plt.plot(forecast, color='r', label="model")
    plt.axvspan(data.index[data.shape[0] - len_test_data - 1], forecast.index[-1], alpha=0.5, color='lightgrey')
    plt.plot(data.actual, label="actual")
    plt.legend()
    plt.grid(True)
    plt.show()
