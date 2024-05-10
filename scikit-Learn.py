"""
from sklearn.family import Model
EX: from sklearn.linear_model import LinearRegression
"""
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import numpy as np
model=LinearRegression()
# model.fit(X=X_train,y=y_train #for training)
# #predictions are through line below
# model.predict(X=x_test)
"""
How to split data into test/training
#Fill this
from sklearn.model_selection import train_test_split
"""
"""
What is Linear Regression?
Determing Best Fit of many data points through bestline.
Basically by taking some unlabeled data, we return back
what we think the labeled data would be
"""
print(model)