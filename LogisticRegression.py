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
# plt.show()
"""
Fill in missing data
"""
print(train.describe())
# print(train.info())
sns.boxplot(x="Pclass",y="Age",data=train)
def impute_age(cols):
    Age = cols[0]
    Pclass=cols[1]
    if pd.isnull(Age):
        if Pclass==1:
            return 37
        elif Pclass==2:
            return 29
        else:
            return 24
    else:
        return Age
train["Age"]=train[["Age","Pclass"]].apply(impute_age,axis=1) #.apply takes the [] as param
"""
Since Cabin column is missing so much info drop col
"""
train.drop("Cabin",axis=1,inplace=True)
sns.heatmap(train.isnull(),yticklabels=False,cbar=False,cmap="viridis")
plt.show()
