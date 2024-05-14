"""
from sklearn.family import Model
EX: from sklearn.linear_model import LinearRegression
"""
# from sklearn.linear_model import LinearRegression
# from sklearn.model_selection import train_test_split
# import numpy as np
# model=LinearRegression()
# # model.fit(X=X_train,y=y_train #for training)
# # #predictions are through line below
# # model.predict(X=x_test)
# """
# How to split data into test/training
# #Fill this
# from sklearn.model_selection import train_test_split
# """
# """
# What is Linear Regression?
# Determing Best Fit of many data points through bestline.
# Basically by taking some unlabeled data, we return back
# what we think the labeled data would be
# """
# print(model)
# """
# Linear Regression Part 1
# """
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("USA_Housing.csv")
# print(df.head())
# print(df.info())
# print(df.describe())
# print(df.columns)
# sns.pairplot(df)
# sns.displot(df["Price"])
# plt.show()
print(df.columns)
X=df[['Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
       'Avg. Area Number of Bedrooms', 'Area Population']]
y=df["Price"]
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.4,random_state=101)
from sklearn.linear_model import LinearRegression
LinearModel=LinearRegression()
LinearModel.fit(X_train,y_train)
print(LinearModel.intercept_)
print(LinearModel.coef_)
cdf=pd.DataFrame(LinearModel.coef_,X.columns,columns=["Coeff"])
print(cdf)
# from sklearn.datasets import fetch_california_housing
# cali=fetch_california_housing()
# print(cali)
predictions=LinearModel.predict(X_test)
print(predictions) #We can compare to y_test
plt.scatter(y_test,predictions)
sns.displot((y_test-predictions)) #Normal dist means correct choice of model
"""
Regression Evaluation MEtrics:
1-MAE (Mean absolute of error)
2-MSE (Mean squared error)
3-RMSE (Root Mean Squared Error Best)
"""
from sklearn import metrics
print(metrics.mean_absolute_error(y_test,predictions))
print(metrics.mean_squared_error(y_test,predictions))
print(metrics.root_mean_squared_error(y_test,predictions))
"""
How to Evaluate model
Finished Part 1 of project,
reached on printing model coefficients
"""

# plt.show()