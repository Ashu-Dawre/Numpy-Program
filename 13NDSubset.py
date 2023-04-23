import numpy as np

arr=np.array([
[10,23,6,9],
[25,73,58,11],
[8,16,32,45]
])

print(arr)
print(arr.shape)

print('all rows with first 2 columns - 0 & 1')
print(arr[:,0:2])

print('all columns for rows 1 & 2')
print(arr[1:,:])

print('all rows after 1 with all columns after 1')
print(arr[1:,1:])

print('from 1st row take 0 column')
print(arr[1:,0])