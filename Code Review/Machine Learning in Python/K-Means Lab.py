# -*- coding: utf-8 -*-
"""
Created on Sun Sep 25 12:56:01 2022

@author: samleo
"""

# import the libraries
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import accuracy_score

# load the Iris dataset with pandas
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
names = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'class']
dataset = pd.read_csv(url, names=names)

X = dataset.values[:,0:4].astype(float)

# Find the optimum number of clusters for k-means
wcss = []  # Within Cluster Sum of Squares
for i in range(1, 11):
    kmeans = KMeans(n_clusters = i, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
    kmeans.fit(X)
    wcss.append(kmeans.inertia_)
    
# Plot the results onto a line graph, allowing us to observe 'The elbow'
plt.plot(range(1, 11), wcss)
plt.title('The elbow method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS') # Within Cluster Sum of Squares
plt.show()

# Apply k-means to the dataset
kmeans = KMeans(n_clusters = 3, init = 'k-means++', max_iter = 300, n_init = 10, random_state = 0)
kmeans.fit(X)
result = kmeans.predict(X)


# Visualize the clusters, plotting features 0 vs 1
plt.scatter(X[result == 0, 0], X[result == 0, 1], s = 100, c = 'red', label = 'Cluster0hi')
plt.scatter(X[result == 1, 0], X[result == 1, 1], s = 100, c = 'blue', label = 'Cluster1')
plt.scatter(X[result == 2, 0], X[result == 2, 1], s = 100, c = 'green', label = 'Cluster2')

# Plot the centroids of the clusters
plt.scatter(kmeans.cluster_centers_[:, 0], kmeans.cluster_centers_[:,1], s = 100, c = 'yellow', label = 'Centroids')

plt.legend()
plt.show()


# Visualize the clusters, plotting features 2 vs 3
plt.scatter(X[result == 0, 2], X[result == 0, 3], s = 100, c = 'red', label = 'Cluster0')
plt.scatter(X[result == 1, 2], X[result == 1, 3], s = 100, c = 'blue', label = 'Cluster1')
plt.scatter(X[result == 2, 2], X[result == 2, 3], s = 100, c = 'green', label = 'Cluster2')

# Plot the centroids of the clusters
plt.scatter(kmeans.cluster_centers_[:, 2], kmeans.cluster_centers_[:,3], s = 100, c = 'yellow', label = 'Centroids')

plt.legend()
plt.show()
