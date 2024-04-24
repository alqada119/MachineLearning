"""
Series
"""
import numpy as np
import pandas as pd

labels=["a","b","c"]
my_data=[10,20,30]
arr=np.array(my_data)
d={"a":10,"b":20,"c":30}
pandas=pd.Series(data=my_data)
print(pandas)
pandas2=pd.Series(data=my_data,index=labels)
print(pandas2)
#basically numpy arr with custom index
pds=pd.Series(arr)
print(pds)
#works with dictionary and uses key as index and value to data
pdd=pd.Series(d)
print(pdd)
#data can be of any type
#To use an index of a series
#fast lookup like hash table
series1=pd.Series([1,2,3],["USA","Italy","GER"])
print(series1)
series2=pd.Series([1,2,5],["USA","Egypt","Italy"])
print(series2)
print(series1["Italy"],series2["Italy"]) #How to access index aka key
print(series1+series2) #Nan if doesn't match

"""
Part 2 Data Frames
"""
from numpy.random import randn
np.random.seed(101) #same random
df=pd.DataFrame(randn(5,4),["A","B","C","D","E"],["W","X","Y","Z"])
print(df) #syntax is (data,rows,col)
#To grab value
print(df["W"])
#Basically data frame is bunch of series with same index (excel)
print(df[["W","Z"]]) #can do multiple cols
df["New"]=df["W"]+df["Y"] #creating new column from current columns
print(df)
#To remove columns
df.drop("W",axis=1,inplace=True) #axis = 1 for columns, axis=0 for row or index
#inplace=True is not default just in case of accident
print(df)
df.drop("E",inplace=True)
print(df)
print(df.shape) #tuple (row,col) hence why row is 0 and col is 1
#To select Rows
print(df.loc["A"])
print(df.iloc[2]) #basically by number indexing
print(df.loc["A","X"]) #row,col
print(df.loc["A"]["X"]) #This also works
"Part 2 of Data Frame"
#Conditional Selection for dataframe
booldf=df>0
print(df[booldf]) #Nan if false
print(df[df["X"]>0]) #conditional of column
print(df[df["Z"]<0])
print(df[df["Z"]<0]["X"])
#Multiple COnditions
print("And",df[((df["X"])>0&(df["Y"]>0))])
print("Or",df[((df["X"])>0|(df["Y"]>0))])
#How to reset index or set index to something else
#reset to default
# df.reset_index(inplace=True)
print(df) #resets to numerical index
newindex="CA NY WY OR".split()
print(newindex)
df["States"]=newindex
print(df)
df.set_index("States",inplace=True)
print(df)
