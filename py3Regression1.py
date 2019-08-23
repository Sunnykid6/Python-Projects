import pandas as pd
import numpy as np
import quandl
import math
from sklearn.model_selection import cross_validate, train_test_split
from sklearn import preprocessing, svm
from sklearn.linear_model import LinearRegression

'''
df = data frame
two dimensional data structure
Pandas data fram consists of
	data, rows, columns
'''
df = quandl.get('WIKI/GOOGL')
df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]
df['Hi-Low_Percent'] = (df['Adj. High'] - df['Adj. Low']) / df['Adj. Low'] * 100.0	
df['Percent_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0	

df = df[['Adj. Close', 'Hi-Low_Percent', 'Percent_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True) 

'''
predicting a new price for the stock
'''
forecast_out = int(math.ceil(0.01 * len(df)))
print(forecast_out)

df['label'] = df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)

X = np.array(df.drop(['label'], 1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]

y = np.array(df['label'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
clf = LinearRegression(n_jobs = 10) #svm.SVR(kernel = 'poly')
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)