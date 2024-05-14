"""
Logistic Regression
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
train=pd.read_csv("titanic_train.csv")
test=pd.read_csv("titanic_test.csv")
# print(train.head())
# print(train.info())
# print(train.describe())
# sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap="viridis")
# sns.set_style('whitegrid')
# # sns.countplot(x="Survived",data=train,hue='Pclass')
# # sns.displot(train.dropna(),x="Age")
# print(train.info())
# # sns.countplot(x="SibSp",data=train)
# sns.displot(x="Fare",data=train)
plt.show()