# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 14:25:27 2018

@author: Varun
"""
# importing library
import numpy as np #mathmatical expression
import matplotlib.pyplot as plt #visualize data 
import pandas as pd  #To read csv by using pandas library

# importing dataset
dataset = pd.read_csv('Data_preprocessing1.csv')
X = dataset.iloc[:, :-1].values
Y = dataset.iloc[:, 3].values

#take care of  missing data
#skitlearn to make machinelearning models
#imputer allows takecare of missing data
#Ctrl+i to inspect object
from sklearn.preprocessing import Imputer
imputer  = Imputer(missing_values = 'NaN')
