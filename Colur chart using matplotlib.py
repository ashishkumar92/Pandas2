import matplotlib.pyplot as plt
import pandas as pd

days=[1,2,3,4,5,6,7]

python=[7,8,6,11,7,8,9]
spark=[2,3,4,3,2,6,5]
pandas=[8,5,7,8,13,5,3]

plt.plot([],[],color='YELLOW',label='python')
plt.plot([],[],color='BLUE',label='spark')
plt.plot([],[],color='ORANGE',label='pandas')
plt.legend()

plt.stackplot(days,python,spark,pandas,colors=["YELLOW","BLUE","ORANGE"])
plt.show()