import numpy as np
import mysql.connector as mycon

con=mycon.connect(host='localhost',user='root',password='volkswagen',database='pysupportdb')

curs=con.cursor()
curs.execute("select balance from accounts;")
data=curs.fetchall()
#print(data)

lst=[]
for rec in data:
   lst.append(rec[0])

#print(lst)

arr=np.array(lst)
print(arr)

con.close()



