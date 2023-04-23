import numpy as np

f=open('accounts.csv','r')
lst=[]

for rec in f:
   try:
      lst.append(float(rec.split(',')[3]))
   except:
      pass

print(lst)
arr=np.array(lst)
print(arr)
print(np.average(arr))
print(np.amax(arr))
print(np.amin(arr))


