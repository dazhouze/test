#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns 

if __name__ == '__main__':
	from sklearn.datasets import make_blobs
	X, y = make_blobs(n_samples=150, n_features=2, centers=3, cluster_std=0.5, shuffle=True, random_state=0)

	fig = plt.figure()
	plt.scatter(X[:,0], X[:,1], c='white', marker='o', edgecolor='black', s=50)
	plt.grid()
	fig.savefig('k_mean.pdf')

	from sklearn.cluster import KMeans
	km = KMeans(n_clusters=3, init='random', n_init=10, max_iter=300, tol=1e-04, random_state=0)
	y_km = km.fit_predict(X)
	
	fig = plt.figure()
	plt.scatter(X[y_km == 0, 0], X[y_km == 0, 1], s=50, c='lightgreen', marker='s', edgecolor='black', label='cluster 1')
	plt.scatter(X[y_km == 1, 0], X[y_km == 1, 1], s=50, c='orange', marker='o', edgecolor='black', label='cluster 2')
	plt.scatter(X[y_km == 2, 0], X[y_km == 2, 1], s=50, c='lightblue', marker='v', edgecolor='black', label='cluster 3')

	plt.scatter(km.cluster_centers_[:, 0], km.cluster_centers_[:, 1], s=250, c='red', marker='*', edgecolor='black', label='centroids')
	plt.legend(scatterpoints=1)
	plt.grid()
	fig.savefig('k_mean2.pdf')
