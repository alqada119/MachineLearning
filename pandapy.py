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
