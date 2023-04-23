import numpy as np

print('Numpy array of strings')
arr=np.array(['soham','sharayu','praffull','java','sql','python'])
print(arr)

print('numpy array of dates')
arr=np.arange("2021-08-09","2021-08-16",dtype="datetime64[D]")
print(arr)

print('business days')
print(np.busday_offset("2021-08-09",7))




