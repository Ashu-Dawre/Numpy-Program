import numpy as np

arr=np.array([9,13,26,1,145,23,67,89,125,173])

res=np.sum(arr)
print('sum of numpy values %d' %res)
res=np.average(arr)
print('average of numpy values %.2f' %res)
res=np.mean(arr)
print('mean of numpy values %.2f' %res)
res=np.median(arr)
print('median of numpy values %.2f' %res)
res=np.corrcoef(arr)
print('correlation coefficient of numpy values %.2f' %res)
res=np.std(arr)
print('standard deviation of numpy values %.2f' %res)
res=np.var(arr)
print('variance of numpy values %.2f' %res)
res=np.amax(arr)
print('largest of numpy values %d' %res)
res=np.amin(arr)
print('smallest of numpy values %d' %res)





