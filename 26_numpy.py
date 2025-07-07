import numpy as np
'''
my_lst=[1,2,3,4,5]
arr=np.array(my_lst)# converting list into an array
print(type(arr))

print(arr.shape)# this function tells no. of rows and colums and for 1 d array it will give no. of elements
'''
"""
# creat 3 list 
lst1=[1,2,3,4,5]
lst2=[2,3,4,5,6]
lst3=[9,7,6,8,9]
arr=np.array([lst1,lst2,lst3])
print(arr)


[[1 2 3 4 5]
 [2 3 4 5 6]
 [9 7 6 8 9]]   # yaha jitne barckets honge uska matlb utne dimentional array hai ye 
 




print(arr.shape) # output will be (3,5) which means 3 rows and 5 colums 
print(arr.reshape(5,3))

[[1 2 3]
 [4 5 2]
 [3 4 5]
 [6 9 7]
 [6 8 9]]
 

print(arr.reshape(1,15))


[[1 2 3 4 5 2 3 4 5 6 9 7 6 8 9]]
"""

l= [1,2,3,4,5]
m=[3,4,5,6,7]
n=[6,7,8,9,9]
arr=np.array([l,m,n])


#indexing

print(arr[0:2,0:2])
arr=np.arange(0,10,2)
print(arr)