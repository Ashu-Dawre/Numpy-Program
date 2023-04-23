import numpy as np

print('numpy array with random numbers')
#arr=np.random.random(9)
arr=np.random.random((3,2))
print(arr)

print('numpy array with random integer numbers')
arr=np.random.randint(1,25,9)
print(arr)

print('pick a random number from numpy array')
x=np.random.choice(arr)
print(x)

print('shuffle elements of numpy')
np.random.shuffle(arr)
print(arr)

