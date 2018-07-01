# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 23:16:42 2018

@author: Varun
"""
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 21:57:28 2018
@author: Varun
"""
""""
Catagorical variable in the dataset is country,purchased columns,
Those variables are catagorical data; 
Country   - France,Germany,spain
Purchased - Yes/No 

Machine learning models, if we keep text some problem, so that 
we need to encode catacombs variables text into numbers
""""
# importing library
import numpy as np #mathmatical expression
import matplotlib.pyplot as plt #visualize data 
import pandas as pd  #To read csv by using pandas library

# importing dataset
dataset = pd.read_csv('Categorical_Data.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

#take care of  missing data
#skitlearn to make machinelearning models
#imputer allows takecare of missing data
#Ctrl+i to inspect object or get help
from sklearn.preprocessing import Imputer
imputer  = Imputer(missing_values = 'NaN', strategy = 'mean', axis = 0)
imputer = imputer.fit(X[:, 1:3])
X[:, 1:3] = imputer.transform(X[:, 1:3])

#Encoding catagorical data
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
labelencoder_X = LabelEncoder()
labelencoder_X.fit_transform(X[:, 0])
X[:, 0] = labelencoder_X.fit_transform(X[:, 0])

#Dummy variable Encoding 
onehotencoder = OneHotEncoder(categorical_features = [0])
X = onehotencoder.fit_transform(X).toarray()

labelencoder_Y = LabelEncoder()
labelencoder_Y.fit_transform(Y)
Y = labelencoder_Y.fit_transform(Y)

#spliting dataset into training set and test set
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.2, random_state = 0)

#Feature scaling
from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X_train = sc_X.fit_transform(X_train)
X_test = sc_X.transform(X_train)

 



