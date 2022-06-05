import matplotlib.pyplot as plt
import statsmodels.tsa.api as smt



    #побудувати графік числових послідовностей значень масиву name_columns криптовалюти df(dataframe)
def graph_timesequences(df, name_columns):
    index = df.index[0]
    title = 'Часова динаміка величин: '
    for name in name_columns:
        title = title + name + ', '
    title = title + ' криптовалюти ' + df.loc[index]['Name']

    fig, ax = plt.subplots(figsize=(15, 10))
    for name in name_columns:
        df[name].plot(ax=ax)
    plt.title(title)
    ax.grid()
    ax.legend()
    plt.show()


    #впобудувати графік числових послідовностей значень масиву name_columns криптовалюти df(dataframe)
        #за інтервал часу [start_date; end_date]
def graph_interval_timesequences(df, name_columns, start_date, end_date):
    index = df.index[0]
    title = 'Часова динаміка величин: '
    for name in name_columns:
        title = title + name + ', '
    title = title + ' криптовалюти ' + df.loc[index]['Name']+\
            ' з ' + start_date + ' по ' + end_date

    fig, ax = plt.subplots(figsize=(15, 10))
    for name in name_columns:
        df[[name]].loc[start_date + ' 00:00:00' : end_date + ' 00:00:00'].plot(ax=ax)
    plt.title(title)
    ax.grid()
    ax.legend()
    plt.show()


    #побудувати графік числових послідовностей значення name_column криптовалют dfs(масив dataframes)
def graph_timesequence_cryptos(dfs, name_column):
    title = 'Часова динаміка величини ' + name_column + '\n криптовалют: '
    for df in dfs:
        title = title + df.loc[df.index[0]]['Name'] + ', '

    fig, ax = plt.subplots(figsize=(15, 10))
    linelegend = []
    for df in dfs:
        df[name_column].plot(ax=ax)
        linelegend.append(df.loc[df.index[0]]['Name'])

    plt.title(title)
    ax.grid()
    ax.legend(linelegend)
    plt.show()


    #побудувати графік числових послідовностей значення name_column криптовалют dfs(масив dataframes)
    # за інтервал часу [start_date; end_date]
def graph_interval_timesequence_cryptos(dfs, name_column, start_date, end_date):
    title = 'Часова динаміка величини ' + name_column + ' з ' + start_date + ' по ' + end_date + '\n криптовалют: '
    for df in dfs:
        title = title + df.loc[df.index[0]]['Name'] + ', '

    fig, ax = plt.subplots(figsize=(15, 10))
    linelegend = []
    for df in dfs:
        df[name_column].loc[start_date + ' 00:00:00' : end_date + ' 00:00:00'].plot(ax=ax)
        linelegend.append(df.loc[df.index[0]]['Name'])

    plt.title(title)
    ax.grid()
    ax.legend(linelegend)
    plt.show()




    #матриця кореляції
def correlation_matrix(df):
    corr = df[['High', 'Low', 'Open', 'Close', 'Volume', 'Marketcap', 'amountToken']].corr()
    print("Matrix correlation" + df.loc[df.index[0]]['Name'])
    print(corr)



def decompose(df):
    decomposition = smt.seasonal_decompose(df[~df.isna()])
    fig = decomposition.plot()
    fig.set_size_inches(15, 10)
    plt.show()


def decompose_interval(df, start_date, end_date):
    decomposition = smt.seasonal_decompose(df.loc[start_date + ' 00:00:00' : end_date + ' 00:00:00'][~df.isna()])
    fig = decomposition.plot()
    fig.set_size_inches(15, 10)
    plt.show()