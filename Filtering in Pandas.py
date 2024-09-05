import pandas as pd

df=pd.read_csv('pokemon.csv')

# df=df.loc[df['Speed']>=100]
# print(df)

fire=df.loc[df['Type 1']=="Fire"]
print(fire)

