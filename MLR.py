'''
importing libraries
'''

import pandas as pd
#import numpy as np
import matplotlib.pyplot as plt

'''
reading and splitting the dataset
''' 
dataset=pd.read_csv("Literacy.csv")
X=dataset.iloc[:,:-1].values
Y=dataset.iloc[:,-1].values

'''
splitting the dataset into train and test set
'''

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test=train_test_split(X,Y,test_size=0.2,random_state=1)

'''
training the Multiple Linear Regression on the dataset
'''
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

'''
predicting the Literacy Rate using the MLR model built above
'''
y_pred=regressor.predict(x_test)
print(y_pred)
print(y_test)


#print(np.concatenate(y_pred.reshape(len(y_pred),1),y_test.reshape(len(y_test),1)),axis=1)
'''
Model Evaluation
'''
import math
from sklearn.metrics import mean_squared_error
'''
Mean Squared Error
'''
print("MSE =",mean_squared_error(y_test,y_pred))

'''
Root Mean Squared Error
'''
print("RMSE =",math.sqrt(mean_squared_error(y_test,y_pred)))

'''
Mean Absolute Error
'''

from sklearn.metrics import mean_absolute_error
print("MAE =",mean_absolute_error(y_test,y_pred))




