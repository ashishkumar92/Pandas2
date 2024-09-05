import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ['Product Id', ' Product Name', ' Country', ' Network Name',
#        ' Supplier Acc Id', ' Supplier Acc Name', ' MCC', ' MNC', ' Priority',
#        ' Routing Criteria', ' Connectivity', ' Cost (USD)',
#        ' Prod Price (USD)', 'Unnamed: 13']
df = pd.read_csv('MMX Product Routing.csv')
# a=df.loc[df[' Country']== 'INDIA']
# a = df[' Product Name'].unique()
# print(df[' Country'].value_counts())
coun_max = (df[' Product Name']).value_counts(normalize=True)
# mxdir = df.groupby(df[' Product Name']=='MxDirect')[' Cost (USD)',' Prod Price (USD)'].max()
dir1 = df.loc[df[' Product Name']=='MxDirect']
us = dir1.loc[dir1[' Country']=='UNITED STATES']

plt.bar(us[' Prod Price (USD)'],us[' Cost (USD)'])
plt.xlabel('Prod Price (USD)')
plt.ylabel('Cost (USD)')
plt.show()
# print(coun_max)
# print(us)