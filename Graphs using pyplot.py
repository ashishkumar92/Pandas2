# import matplotlib.pyplot as plt
#
# name=['a','b','c','d','e','f']
# j=[1,2,3,4,5,6]
# k=[1.5,2.5,3.5,4.5,5.5,6.5]
# runs=[5,10,20,15,10,20]
# run2=[10,20,30,5,20,15]
#
# plt.bar(j, runs, width=0.3,align='edge')
# plt.bar(k, run2, width=0.3,)
#
# plt.xticks(j,name)
#
# plt.show()


l1 = [1,2,3,4]
l2= [1,2,3]
l1=l2
print(l1)
print((1<=5<=10) and not len(""))
def x(a,b,c):
    print(a,b,c)
l= [1,2,3]
x(*l)
a=[1 if i%2 else 0 for i in range(6)]
print(a)

import pandas as pd
import mysql.connector as mc

myco = mc.connect(host='localhost',user='root',password='root123',database='ashish')

# q = 'select * from student'
q = 'select * from wallmart'
df = pd.read_sql(q,myco)
print(df)
# df['len']= df['First Name'].str.len()
# print(df)
