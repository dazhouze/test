#!/usr/bin/env python3.5
# -*- coding: utf-8 -*-

import pandas as pd
import matplotlib as mpl
mpl.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.backends.backend_pdf
import numpy as np
import tensorflow as tf

def conv1d(x, w, p=0, s=1):
	w_rot = np.array(w[::-1])
	x_padded = np.array(x)
	if p > 0:
		zero_pad = np.zeros(shape=p)
		x_padded = np.concatenate([zero_pad, x_padded, zero_pad])
	res = []
	for i in range(0, int(len(x)/s), s):
		res.append(np.sum(x_padded[i:i+w_rot.shape[0]] * w_rot))
	return np.array(res)

import scipy.signal
def conv2d(X, W, p=(0, 0), s=(1, 1)):
	W_rot = np.array(W)[::-1, ::-1]
	X_orig = np.array(X)
	n1 = X_orig.shape[0] + 2*p[0]
	n2 = X_orig.shape[1] + 2*p[1]
	X_padded = np.zeros(shape=(n1, n2))
	X_padded[p[0]:p[0]+X_orig.shape[0], p[1]:p[1]+X_orig.shape[1]] = X_orig
	res = []
	for i in range(0,  int((X_padded.shape[0] - W_rot.shape[0])/s[0])+1, s[0]):
		res.append([])
		for j in range(0, int((X_padded.shape[1] - W_rot.shape[1])/s[1])+1, s[1]):
			X_sub = X_padded[i:i+W_rot.shape[0], j:j+W_rot.shape[1]]
			res[-1].append(np.sum(X_sub * W_rot))
	return(np.array(res))

if __name__ == '__main__':
	x = [1, 3, 2, 4, 5, 6, 1, 3]
	w = [1, 0, 3, 1, 2]
	print('Conv1d implementation:', conv1d(x, w, p=2, s=1))
	print('Numpy Results:', np.convolve(x, w, mode='same'))

	X = [[1,3,2,4], [5,6,1,3], [1,2,0,2], [3,4,3,2]]
	W = [[1,0,3], [1,2,1], [0,1,1]]
	print('Conv2d Implemetation:\n', conv2d(X, W, p=(1,1), s=(1,1)))
	print('Scipy Results:\n', scipy.signal.convolve2d(X, W, mode='same'))
