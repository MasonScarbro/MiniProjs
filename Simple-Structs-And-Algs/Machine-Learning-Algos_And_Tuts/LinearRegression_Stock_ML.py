import pandas as pd 
import quandl
import math
from datetime import datetime
import matplotlib.pyplot as plt
import numpy as np
from sklearn import preprocessing, model_selection, svm 
from sklearn.linear_model import LinearRegression
from matplotlib import style
import pickle 

style.use('ggplot')

df = quandl.get('WIKI/GOOGL')

df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

#This is stock stuff which isnt really important but esiantially it is a row by row where apparentl trhe high low percentage change is this equation the adj high - the adj close / adj close (and for the percent we mult by 100)
df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0 
# same here basically ^
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0 

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True) #fills any NaN data with -99999, why? because we dont whant any data to be missing and bc the way ML works it cant work with NaN data

''' forecast_out: This is a bit confusing but what this is is exactly what the 
    var says its the future prediction of the stock price
    in days so this is predicting 10% of the data frame and 
    rounding it to an integer in case its a float and or a small decimal like .2 
    predicting out 10% of the data frame which might be days by using the last 10% to predict the next
    you can of course change this value '''
forecast_out = int(math.ceil(0.01*len(df)))

''' df['label']: tho this looks weird is actually quite simple essiantially 
    you are adjusting the columns "negativley" so as to shift the columns up
    therefore the next rows will be the forecast_col i.e the Adj. Close 10 days in the future'''
df['label'] = df[forecast_col].shift(-forecast_out) 


X = np.array(df.drop(['label'], axis=1)) #Features: Everything other than the label, (dropss the label and creates a new dataframe without the label)
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out]
 

df.dropna(inplace=True)
y = np.array(df['label']) #Label: the label 

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y, test_size=0.2)

clf = LinearRegression()
clf.fit(X_train, y_train)

#saves the classifier to a pickle post training 
with open('linearregression.pickle', 'wb') as f:
    pickle.dump(clf, f)
pickle_in = open('linearregression.pickle', 'rb')
clf = pickle.load(pickle_in)


accuracy = clf.score(X_test, y_test)

print(accuracy)

forecast_set = clf.predict(X_lately)
print(forecast_set, accuracy, forecast_out)

df['Forecast'] = np.nan

last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day
''' this is just plot manipulation in order to have the dates on the axis  
    the next date is the timestamp of the last day + one more day
    then increment the next_unix and make sure to get rid of any unwanted nan with the forecasted value'''

for i in forecast_set:
    next_date = datetime.fromtimestamp(next_unix) 
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show() 
