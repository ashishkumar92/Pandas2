import psycopg2
import pandas as pd
import os

conn = psycopg2.connect(
   database="SuperMart_DB", user='postgres', password='root123', host='127.0.0.1', port= '5432'
)


q1='select * from Customer'
q2 ='select * from Product'
q3 ='select * from Sales'
df_cus = pd.read_sql(q1,conn)
df_Pro = pd.read_sql(q2,conn)
df_Sal = pd.read_sql(q3,conn)
# print(df_cus.info(),df_Pro.info(),df_Sal.info())

df = df_Sal.merge(df_Pro, on= 'product_id')
df1=df[['order_date','customer_id','product_id','product_name','quantity','sales','profit']]
# df1.to_csv(r'C:\Users\Ashish Kumar\Desktop\SalesData.csv')
a=(df1.loc[df1['profit']>300])
print(a)
