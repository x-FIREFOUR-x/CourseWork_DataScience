from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_percentage_error
import pylab
import matplotlib.pyplot as plt
import scipy.stats as stats


    #split dataframe to train and test dataframes (timeseries)
def train_test_data(df, column, len_train_data, len_test_data=365):
    dfs = df
    if ((len_train_data + len_test_data <= df.shape[0]) and (len_train_data > 0) and len_test_data > 0):
        dfs = dfs[dfs.shape[0]-len_train_data-len_test_data:]
    else:
        len_test_data = (int)(dfs.shape[0] / 5)
        len_train_data = dfs.shape[0] - len_test_data

    train_date = dfs[0: len_train_data]
    test_date = dfs[len_train_data:]

    return (dfs, train_date, test_date, len_train_data, len_test_data)


def metrics(test, model):
    forecast = model.predict(start=test.index[0], end=test.index[-1])

    mse = mean_squared_error(test, forecast)
    r2 = r2_score(test, forecast)
    mape = mean_absolute_percentage_error(test, forecast)

    print('    Metrics:')
    print('mean squared error = ', mse)
    print('r2 = ', r2)
    print('mean absolute percentage error = ', mape)
    print('\n')

def qq_plot(series):
    stats.probplot(series, dist="norm", plot=pylab)
    pylab.show()

def st_residual_plot(test, model):
    forecast = model.predict(start=test.index[0], end=test.index[-1])
    series = test-forecast
    mean = series.mean()
    std = series.std()
    standardized_residuals = (series - mean)/std
    plt.figure(figsize=(12, 6))
    plt.title("Standardized residuals")
    plt.plot(standardized_residuals)
    plt.grid(True)
    plt.show()