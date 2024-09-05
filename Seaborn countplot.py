import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('pokemon.csv')
sns.countplot(y='Type 1',data=df)
plt.show()