import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from mlpca import MLPCA
from sklearn.decomposition import PCA

iris = load_iris()
train_X, test_X, train_y, test_y = train_test_split(iris['data'], iris['target'], random_state=0)
train = np.mat(train_X)
test = np.mat(test_X)
a = np.random.rand(448).reshape(112,4)
b = np.random.rand(152).reshape(38,4)
train_err = np.multiply(train,a)
test_err = np.multiply(test,b)
# Xsd = np.loadtxt('./1.csv', delimiter=",", skiprows=1)
# U, S, V = MLPCA(X, Xsd)
# result = U @ S @ V.T
train_PCA = MLPCA(train,train_err)
test_PCA = MLPCA(test,test_err)

from sklearn.linear_model import LogisticRegression
from sklearn import metrics
model1 = LogisticRegression()
model1.fit(train_X, train_y)
prediction = model1.predict(test_X)
print('The accuracy of the Logistic Regression is: {0}'.format(metrics.accuracy_score(prediction,test_y)))
model2 = LogisticRegression()
model2.fit(test, test_y)
prediction = model2.predict(test_X)
print('The accuracy of the Logistic Regression is: {0}'.format(metrics.accuracy_score(prediction,test_y)))
# print(result)

model3 = LogisticRegression()
pca = PCA(n_components=0.99)
principalComponents = pca.fit_transform(train_X)
# 查看降维后的数据
import pandas as pd
principalDf = pd.DataFrame(data=principalComponents)
model3.fit(principalDf, test_y)
prediction = model3.predict(test_X)
print('The accuracy of the Logistic Regression is: {0}'.format(metrics.accuracy_score(prediction,test_y)))