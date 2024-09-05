import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

a = sns.get_dataset_names()
# print(a)
df = sns.load_dataset('tips')
# print(df.head())
c = {'No':'RED','Yes':'Orange'}
# sns.scatterplot(x='total_bill',y='tip',hue='smoker',hue_order=['No','Yes'],palette=c,data=df)
sns.relplot(x='total_bill',y='tip',data=df,row='size')
plt.show(block=True)   # block= True if fig close suddenly and not able to see fig.
