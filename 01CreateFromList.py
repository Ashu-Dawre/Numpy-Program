import numpy as np

print('Creating numpy array using a list')
lst=[13,9,1,26,45,23,89,25,78]
arr=np.array(lst)
print(type(lst))
print(lst)
print(type(arr))
print(arr)

for i in range(len(lst)):
    lst[i]=lst[i]**2
print(lst)

arr=arr**2
print(arr)



