from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_percentage_error


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
    mbpe = mean_absolute_percentage_error(test, forecast)

    print('mean squared error = ', mse)
    print('r2 = ', r2)
    print('mean absolute percentage error = ', mbpe)
