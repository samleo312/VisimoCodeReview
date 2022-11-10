# -*- coding: utf-8 -*-
"""
Created on Sat Sep 24 21:42:34 2022

@author: samleo
"""

from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import numpy as np 
import pandas as pd

# load the Iris dataset with pandas
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'label']
dataset = pd.read_csv(url, names=names)

# Data set
X = dataset.values[:,0:4].astype(float)
# Labels
Y = dataset.values[:,4].astype(str)


# Training data set
X_train = X[:125,:]
# Corresponding training labels
y_train = Y[:125]


# Test data set
X_test = X[25:,:]
# Corresponding test labels
y_test = Y[25:]


# Decision tree learning
dt = DecisionTreeClassifier()

dt.fit(X_train, y_train)

# Predictions
print("Predicting labels")
results = dt.predict(X_test)


accuracy = accuracy_score(y_test,results)
print ("Accuracy: ", accuracy)

# Are the predicted results correct? Calculate accuracy by comparing results to the actual y_test labels
#1A: Accuracy: 0.33
#1B Accuracy: 0
#1C: Accuracy: 0.976