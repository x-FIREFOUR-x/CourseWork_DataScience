import warnings                                  # do not disturbe mode
warnings.filterwarnings('ignore')

# Load packages
import numpy as np                               # vectors and matrices
import pandas as pd                              # tables and data manipulations
import matplotlib.pyplot as plt                  # plots
import seaborn as sns                            # more plots

from dateutil.relativedelta import relativedelta # working with dates with style
from scipy.optimize import minimize              # for function minimization

import statsmodels.formula.api as smf            # statistics and econometrics
import statsmodels.tsa.api as smt
import statsmodels.api as sm
import scipy.stats as scs

from itertools import product                    # some useful functions
from tqdm import tqdm_notebook

from sklearn.metrics import r2_score, median_absolute_error, mean_absolute_error, mean_absolute_percentage_error
from sklearn.metrics import median_absolute_error, mean_squared_error, mean_squared_log_error

def SARIMA(df, column):
    ps = range(2, 5)
    d = 1
    qs = range(2, 5)
    Ps = range(0, 2)
    D = 1
    Qs = range(0, 2)
    s = 24  # season length is still 24

    # creating list with all the possible combinations of parameters
    parameters = product(ps, qs, Ps, Qs)
    parameters_list = list(parameters)
    len(parameters_list)

    '''
    result_table = optimizeSARIMA(df, column, parameters_list, d, D, s)

    p, q, P, Q = result_table.parameters[0]

    best_model = sm.tsa.statespace.SARIMAX(df[column], order=(p, d, q),seasonal_order=(P, D, Q, s)).fit(disp=-1)

    print(best_model.summary())

    plotSARIMA(df[column], best_model, 50, s, d)
    '''

    best_model = sm.tsa.statespace.SARIMAX(df[column].head(10), order=(4, d, 4), seasonal_order=(1, D, 1, s)).fit(disp=-1)
    plotSARIMA(df[column], best_model, 50, s, d)



def optimizeSARIMA(df, column, parameters_list, d, D, s):
    """Return dataframe with parameters and corresponding AIC

        parameters_list - list with (p, q, P, Q) tuples
        d - integration order in ARIMA model
        D - seasonal integration order
        s - length of season
    """

    results = []
    best_aic = float("inf")
    serias = df[column]

    for param in parameters_list:
        # we need try-except because on some combinations model fails to converge
        try:
            model = sm.tsa.statespace.SARIMAX(df[column],
                                              order=(param[0], d, param[1]),
                                              seasonal_order=(param[2], D, param[3], s)
                                              ).fit(disp=-1)
        except:
            continue
        aic = model.aic
        # saving best model, AIC and parameters
        if aic < best_aic:
            best_model = model
            best_aic = aic
            best_param = param

        print(param, model.aic)
        results.append([param, model.aic])

    result_table = pd.DataFrame(results)
    result_table.columns = ['parameters', 'aic']

    # sorting in ascending order, the lower AIC is - the better
    result_table = result_table.sort_values(by='aic', ascending=True).reset_index(drop=True)

    return result_table


def plotSARIMA(series, model, n_steps, s, d):
    """Plots model vs predicted values
        series - dataset with timeseries
        model - fitted SARIMA model
        n_steps - number of steps to predict in the future
    """

    '''
    fig, ax = plt.subplots(figsize=(15, 10))
    fig.suptitle('Прогноз опадів на 2018 рік', fontsize=16)
    ax = series.loc[series.index[-300:]].plot()
    #ax.vlines(series.index[-1], 0, 1.5, linestyle='--', color='r')
    ax = model.predict(series.index[0], series.index[-1], dynamic=True, plot_insample=False, ax=ax).plot()
    plt.show()
    '''


    # adding model values
    data = series.copy()
    data = pd.DataFrame(list(data), columns=['actual'], index=data.index)
    data['sarima_model'] = model.fittedvalues

    # making a shift on s+d steps, because these values were unobserved by the model
    # due to the differentiating
    data['sarima_model'][:s + d] = np.NaN

    #print(data.head(10))

    # forecasting on n_steps forward
    forecast = model.predict(start=data.shape[0], end=data.shape[0] + n_steps)
    forecast = data.sarima_model.append(forecast)
    # calculate error, again having shifted on s+d steps from the beginning
    #error = mean_absolute_percentage_error(data['actual'][s + d:], data['sarima_model'][s + d:])

    plt.figure(figsize=(15, 7))
    #plt.title("Mean Absolute Percentage Error: {0:.2f}%".format(error))
    plt.plot(forecast, color='r', label="model")
    plt.axvspan(data.index[-1], forecast.index[-1], alpha=0.5, color='lightgrey')
    plt.plot(data.actual, label="actual")
    plt.legend()
    plt.grid(True)
    plt.show()




