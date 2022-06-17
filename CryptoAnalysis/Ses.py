import pandas as pd                              # tables and data manipulations
import matplotlib.pyplot as plt                  # plots

from statsmodels.tsa.holtwinters import SimpleExpSmoothing

from Models import *


    # model Simple Exponent Smoothing(SES)
def SES(df, column, len_train=0, len_test=0, len_forcast=50):
    """model Simple Exponent Smoothing
            df - dataframe timeseries
            column - name column with timeserias in dataframe
            len_train - number day train data
            len_test - number day test data
            len_forcast - number day predict in the future
    """

    # split dataframe to train and test dataframe (timeseries)
    dfs, train_df, test_df, len_train, len_test = train_test_data(df, column, len_train, len_test)

    # build model
    model = SimpleExpSmoothing(train_df[column]).fit()
    print(model.summary())

    # build plot
    plotSES(dfs[column], column, model, len_test, len_forcast)



    # build plot Simple Exponent Smoothing
def plotSES(series, column, model, len_test_data, len_forcast):
    """Plots model vs predicted values
        series - dataset with timeseries
        column - column timeserias in serias
        model - fitted SES Simple Exponent Smoothing model
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
    plt.title("Forkast model Simple Exponent Smoothing, column: " + column)
    plt.plot(forecast, color='r', label="model")
    plt.axvspan(data.index[data.shape[0] - len_test_data - 1], forecast.index[-1], alpha=0.5, color='lightgrey')
    plt.plot(data.actual, label="actual")
    plt.legend()
    plt.grid(True)
    plt.show()



