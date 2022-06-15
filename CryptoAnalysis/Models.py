
    #split dataframe to train and test dataframes (timeseries)
def train_test_data(df, column, len_train_data, len_test_data=365):
    dfs = df
    if (len_train_data + len_test_data <= df.shape[0]):
        dfs = dfs[dfs.shape[0]-len_train_data-len_test_data:]
    else:
        len_test_data = (int)(dfs.shape[0] / 5)
        len_train_data = dfs.shape[0] - len_test_data

    train_date = dfs[0: len_train_data]
    test_date = dfs[len_train_data+1:]

    return (dfs, train_date, test_date, len_train_data, len_test_data)