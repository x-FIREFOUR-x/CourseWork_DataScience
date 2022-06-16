from statsmodels.tsa.holtwinters import SimpleExpSmoothing

import pandas as pd                              # tables and data manipulations
import matplotlib.pyplot as plt                  # plots

from Models import *


from statsmodels.tsa.api import VAR
from statsmodels.tsa.statespace.varmax import VARMAX




def SES(df, column):

    # split dataframe to train and test dataframe (timeseries)
    len_test = 20
    len_train = 250
    dfs, train_df, test_df, len_train, len_test = train_test_data(df, column, len_train, len_test)


    # build best model
    model = SimpleExpSmoothing(train_df[column]).fit()

    print(model.summary())

    # build plot
    plotSES(dfs[column], column, model, len_test, 50)

    '''
    len_test = 20
    len_train = 255
    dfs, train_df, test_df, len_train, len_test = train_test_data(df, column, len_train, len_test)

    best_model = sm.tsa.statespace.SARIMAX(train_df[column], order=(4, d, 4), seasonal_order=(1, D, 0, s)).fit(disp=-1)
    plotSARIMA(dfs[column], column, best_model, len_test, 50, s, d)
    '''




def plotSES(series, column, model, len_test_data, len_forcast):
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

    plt.figure(figsize=(15, 7))
    plt.title("Forkast model SARIMAX, column: " + column)
    plt.plot(forecast, color='r', label="model")
    plt.axvspan(data.index[data.shape[0] - len_test_data - 1], forecast.index[-1], alpha=0.5, color='lightgrey')
    plt.plot(data.actual, label="actual")
    plt.legend()
    plt.grid(True)
    plt.show()



