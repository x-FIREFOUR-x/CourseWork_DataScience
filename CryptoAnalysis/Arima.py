import statsmodels.tsa.api as smt
import matplotlib.pyplot as plt

from Analysis import *


def model_arima(df, column, p, d, q):
    train_data = df[column].loc[df.index[0:]]
    print(train_data.head(10))
    train_data.describe()
    print(train_data.head())

    '''
    d = 0
    if(dickey_fuller_test(df, column)):
        d = 0
    else:
        d = 1
    '''

    #model = smt.ARIMA(train_data, order=(1, 0, 1)).fit()
    model = smt.ARIMA(train_data, order=(p, d, q)).fit()
    model.summary()
    print(model.summary())

    fig, ax = plt.subplots(figsize=(15, 10))
    fig.suptitle('Прогноз', fontsize=16)
    ax = train_data.loc[train_data.index[-365:]].plot()
    ax.vlines(train_data.index[-1], 0, 1.5, linestyle='-', color='r')
    model.predict(train_data.index[-365], df.index[-1], dynamic=True, plot_insample=False, ax=ax).plot()
    plt.show()