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
"""
Data Frames Part 3
"""
outside=["G1",'G1','G1','G2',"G2","G2"]
inside=[1,2,3,1,2,3]
hier_index=list(zip(outside,inside))
hier_index=pd.MultiIndex.from_tuples(hier_index)
print(hier_index)
df=pd.DataFrame(randn(6,2),hier_index,["A","B"])
print(df.loc['G1'].loc[1])#index of outside then index of inside
print(df.index.names) #names of index's
df.index.names=["Groups","Num"] #multi-index names
print((df.loc["G2"].loc[2]))
#Cross section
print(df.xs("G1")) # same as df.loc["G1"]
#or can get you an index from two different outer index
print(df.xs(1,level="Num"))
#Lessosn Learned are multiindex, grabbing from multindex and cross section
"""
Part 4: Missing Data
"""
d={"A":[1,2,np.nan],'B':[5,np.nan,np.nan],'C':[1,2,3]}
df=pd.DataFrame(d)
print(df)
#How to drop missing values
# df=df.dropna(axis=0) #row
# df=df.dropna(axis=1) #col
# df=df.dropna(thresh=2)
print(df) #sicne row 1 has atleast 2 non na value swe keep it
df=df.fillna(value="Missing")
print(df) #fill missing value
"""
Groupby
"""
data={'Company':['Google','Google',"Microsoft",'Microsoft','Microsoft','Meta'],'Person':['Ahmed','Anas','Donna','Tala','Isaac','Christian'],'Sales':[100,120,140,160,180,200]}
exceldf=pd.DataFrame(data)
exceldf.index.names=["Order"]
print(exceldf)
Comp=exceldf.groupby('Company') #GroupBy returns an object which you can perform multiple aggregate functions on
print(Comp.mean(numeric_only=True)) # New change now standard is False for this
print(Comp.sum().loc["Meta"]) #Get specific Meta Sum
print(Comp.count()) # 3 people work for microsoft and 3 sales for them etc
print(Comp.describe().transpose()) #Get all aggregate functions VVVV Important
"""
Concatentation
"""
df1=pd.DataFrame({'Key':[1,2,3],'A':["A","B","C"],'B':["D","E","F"]})
df2=pd.DataFrame({'Key':[1,2,4],'C':["C","C","C"],'D':["D","E","F"]})
df3=pd.concat([df1,df2])
print(df3) #concatetated by row
df4=pd.concat([df1,df2],axis=1) #by col most used
print(df4)
df5=pd.merge(df1,df2,how='inner',on='Key') #on is the most important part, where they share keys merge
print(df5)
#You can also pass on list of on
# df6=pd.merge(df1,df2,on=["Key","sth"])
#Join
#Join is merge done on two different index columns
# df=pd.DataFrame({
#     "col1":[100,123,145],
#     "col2":[100,3,145],
#     "col3":[100,123,145]
# })
# print(df)
# print(df.head())
# print(df["col2"].unique())
# print(df.index)
# df.sort_values(by="col2")
# print(df)
# print(df.columns)
# print(df.isnull()) #Very Useful
"""
Read and write pandas
"""
# df=pd.read_csv("example.csv")
# print(df) #How to read
df=pd.DataFrame({"Test":[1,2,3]})
df.to_csv("My_output",index=False)
print(pd.read_csv("My_output"))
# print(pd.read_excel("Excel.xlsx",sheet_name="Sheet1")) #How to read from excel
# df.to_excel("Test.xlsx",sheet_name="Sheet1")
# data=pd.read_html("https://www.fdic.gov/resources/resolutions/bank-failures/failed-bank-list/index.html")
# print(data)
#How to read sql
# from sqlalchemy import create_engine
# engine=create_engine("sqlite:///:memory:")
# df.to_sql("my_table",engine)
# sqldf=pd.read_sql("my_table",con=engine)
# print(sqldf)
"""
Matplot Lib
"""
import matplotlib.pyplot as plt
plt.show()
x=np.linspace(0,5,11)
y=x**2
print(x,y)
# #functional
# plt.plot(x,y)
# # plt.show() #How to show the plt
# plt.xlabel("X Label")
# plt.ylabel("Y Label")
# plt.title("Title")
# plt.show()
# plt.subplot(1,2,1)
# plt.plot(x,y,"r")
# plt.subplot(1,2,2)
# plt.plot(y,x)
# plt.show()

"""
Object Oriented
"""
# fig=plt.figure()
# axes=fig.add_axes((0.1,0.1,0.8,0.8))
# axes2=fig.add_axes((0.2,0.5,0.4,0.3))
# #Left Bottom Width Height in relation to canvas
# axes.plot(x,y)
# axes.set_title("Main")
# axes.set_xlabel("X Label")
# axes.set_ylabel("Y Label")
# axes2.plot(y,x)
# axes2.set_title("Inverse")
fig,axes=plt.subplots(nrows=1,ncols=2)
# axes.plot(x,y)
# for curr in axes:
#     curr.plot(x,y)
axes[0].plot(x,y)
axes[1].plot(y,x)
axes[0].set_title("First")
axes[1].set_title("Second")
plt.show()
"""
Second method of subplots much easier than manual way above
"""



