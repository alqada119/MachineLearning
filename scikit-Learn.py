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
# from sklearn import metrics
# print(metrics.mean_absolute_error(y_test,predictions))
# print(metrics.mean_squared_error(y_test,predictions))
# print(metrics.root_mean_squared_error(y_test,predictions))
"""
How to Evaluate model
Finished Part 1 of project,
reached on printing model coefficients
"""
customers=pd.read_csv("Ecommerce Customers")
print(customers.head())
print(customers.info())
X=customers[['Avg. Session Length', 'Time on App',
       'Time on Website', 'Length of Membership']]
y=customers["Yearly Amount Spent"]
print(X.shape,y.shape)
X_train,y_train,X_test,y_test=train_test_split(X,y,test_size=0.3,random_state=101)
lm=LinearRegression()
lm.fit(X_train,y_train)
# print(lm.coef_)
# plt.show()
"""
Error Faced:
Found input variables with inconsistent numbers of samples: [350, 150]
"""

"""
Logistic Regression is another binary classification model.
Unlike Linear which is one continous value.
Sigmoid aka logistic outputs between 0-1
f(x)=1/(1+e^-x) #always 0-1
The key here is that the y value will always be
that after the cutoff point usually 0.5
2 classes generate meaning
if less than 0.5 then 0 class
if more than 0.5 then 1 class
This model's test data is evaluated by
a confusion matrix.
Example Testing for a disease
165 tests done
TP: predicted positive and is actual P
TN: predicted negative and is actual N
Adding both of those and dividing by total
gets you accuracy.
FP: predicted positive but actual not P Type1
FN: predicted negative but actual not N Type2
Example:
TN=50,TP=100 then 150/165=91%
Error Rate= 15/165 =9%
"""