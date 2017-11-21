import pandas as pd
import numpy as np
from matplotlib import pyplot as pl

def readFile(path):
    excel = pd.ExcelFile(path)
    data = excel.parse("Sheet1")
    parsed = pd.io.excel.ExcelFile.parse(excel, "Sheet1")
    listColumn = parsed.columns

    data = np.array(data)
    return listColumn, data

def readData(data):
    n = np.shape(data)[0]
    m = np.shape(data)[1]

    X = data[:, 0:m -1]
    y = data[:, m-1:m]

    mu = np.mean(X)
    sigma = np.std(X)
    X = (X - mu) / sigma
    X = np.insert(X,0, 1, axis=1)
    return X, y, mu, sigma

def strain(pathfile):
    listColumn, data = readFile(pathfile)
    X, y, mu, sigma = readData(data)
    n = np.shape(data)[0]
    m = np.shape(data)[1]
    alpha = 0.01
    num_iters = 500

    theta = np.zeros((m,1))

    for iter in range(1, num_iters):
        h = np.dot(X,theta)
        theta = theta - alpha * np.dot(X.T,(h - y))/n
    return theta, mu, sigma

def predict(X, theta, mu, sigma):
    X = (X - mu) / sigma
    X = np.insert(X, 0, 1, axis=1)
    return X.T * theta


