import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = sns.load_dataset('tips')
sns.catplot(x='total_bill',y='day',data=df,kind='boxen')  # kind can be bar, line,point, violin,boxen etc
# sns.catplot(x='time',y='tip',data=df)  # catplot is best if one value is categorical and other is numerical.
plt.show()