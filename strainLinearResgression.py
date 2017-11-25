import numpy as np
import pandas as pd


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

    X = data[:, 0:m - 1]
    y = data[:, m - 1:m]

    mu = np.mean(X, axis=0)
    sigma = np.std(X, axis=0)
    X = (X - mu) / sigma
    X = np.insert(X, 0, 1, axis=1)
    return X, y, mu, sigma


def strain(pathfile):
    listColumn, data = readFile(pathfile)
    X, y, mu, sigma = readData(data)
    n = np.shape(data)[0]
    m = np.shape(data)[1]
    alpha = 0.01
    num_iters = 500

    theta = np.zeros((m, 1))

    for iter in range(1, num_iters):
        h = np.dot(X, theta)
        theta = theta - alpha * np.dot(X.T, (h - y)) / n
    listColumn = list(listColumn)
    return listColumn, theta, mu, sigma


def predict(X, theta, mu, sigma):
    X = (X - mu) / sigma
    X = np.insert(X, 0, 1, axis=0)
    return np.dot(X.T,theta)

def demo():
    A=[]
    for i in range(0, 3):
        A.append(str(i))
    return A

if __name__ == "__main__":
     A = demo()
     print A
     print "param"+str(5)


#print listColumn[1]
