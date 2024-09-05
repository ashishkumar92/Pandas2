import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv('pokemon.csv')

fire = data.loc[data['Type 1']=='Fire']
grass = data.loc[data['Type 1']=='Grass']

plt.scatter(grass['Attack'],grass['Defense'],label='Grass')
plt.scatter(fire['Attack'],fire['Defense'],label='Fire')
plt.legend()
plt.grid()
plt.title('pokemon')
plt.xlabel('attack')
plt.ylabel('defense')
plt.show()