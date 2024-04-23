"""
Following the udemy course, I will use this file to demonstrate udemy learning!
"""
import numpy as np
arr=np.array([1,2,3])
matrix=np.array([[1,2,3],[1,2,3],[1,2,3]])
print(arr,matrix)
arrange=np.arange(0,10) #arr of range (0,10) - also takes step size
print(arrange)
ze=np.zeros(3) #3 0s
zer=np.zeros((5,5)) #row,col
print(zer)
#same thing with ones
one=np.ones((5,5))
print(one)
lint=np.linspace(0,5,10)
print(lint) # 10 evenly spaced numbers between 0 and 5
eye=np.eye(4)
print(eye) #square matrix of 4 row 4 col
rand=np.random.rand(5,5) #0 to 1 for 2d comma separated row,col
print(rand)
randn=np.random.randn(2)
print(randn)
randomlow=np.random.randint(0,10,(5,5)) # random between 0 and 9 inclusive
print(randomlow)
arr=np.arange(0,25)
print(arr)
changed=arr.reshape(5,5)
print(changed) #reshape is a useful function that transforms arr to matrix of choice dimensions as long as dimensions possible
print(changed.max(),changed.min() )# gets max,min
print(changed.argmax(),changed.argmin()) #gets index of min and max
#to get shape of matrix
print(changed.shape) #attribute of np arr is shape
#to get type of np arr
print(changed.dtype)
#np.arr converts to 2d arr
