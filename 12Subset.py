import numpy as np

arr=np.array([9,13,26,1,145,23,64,89,125,178])
print('whole array')
print(arr)

print('elements from 3 onwards')
print(arr[3:])

print('elements upto 6 from the beginning')
print(arr[:6])

print('part of NP array')
print(arr[3:7])

print('negative indexing')
print(arr[-1])

print('conditional retrieval of elements')
print(arr[arr%2==0])

print('condition status')
print(arr%2==0)



