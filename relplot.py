import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')
sns.relplot(x='total_bill',y='tip',data=df,row='time',col='smoker',kind='bar')
plt.show(block=True)  # Only relplot is best for showing sub-plotting. It has so many parameter like hue, alpha etc.