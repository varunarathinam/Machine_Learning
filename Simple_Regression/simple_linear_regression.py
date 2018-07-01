# -*- coding: utf-8 -*-
"""
Created on Sun Mar  4 09:11:19 2018

@author: Varun
"""
#Simple Linear Regression
#matrix of independent variable of X (19,1)
#vector of dependent variable of Y (19, )
# importing library
import numpy as np #mathmatical expression
import matplotlib.pyplot as plt #visualize data 
import pandas as pd  #To read csv by using pandas library

# importing dataset
dataset = pd.read_csv('Salary_Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 1].values

#spliting dataset into training set and test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 1/3, random_state = 0)

"""#Feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_train)"""

#Fitting Simple linear regression to training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)

#Predicting the test set results
y_pred = regressor.predict(X_test)

#Visualising the training set results
plt.scatter(X_train, y_train, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Traing set)')
plt.xlabel('Year of experience')
plt.ylabel('Salary')
plt.show()


plt.scatter(X_test, y_test, color = 'red')
plt.plot(X_train, regressor.predict(X_train), color = 'blue')
plt.title('Salary vs Experience (Traing set)')
plt.xlabel('Year of experience')
plt.ylabel('Salary')
plt.show()


