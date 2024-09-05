import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df= sns.load_dataset("flights")
# print(df)
max=df.groupby("year")["passengers"].max().reset_index()
mean=df.groupby("year")["passengers"].mean().reset_index()
median=df.groupby("year")["passengers"].median().reset_index()
plt.bar(max["year"],max["passengers"])
plt.plot(mean["year"],mean["passengers"],color="Red")
plt.plot(median["year"],median["passengers"],color="Yellow")
plt.show()