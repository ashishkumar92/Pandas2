import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('pokemon.csv')
ef = df.loc[df['Type 1']=='Fire']
df = df.loc[df['Type 1']!='Fire']

plt.scatter(df['Defense'],df['Attack'])
plt.scatter(ef['Defense'],ef['Attack'])


plt.show()