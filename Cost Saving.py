import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ['Month', 'Proactive - Cost Saving Changes(Count)',
#        'Proactive - Cost Saving  $',
#        'Proactive Quality Improvement Changes(Count)',
#        'Reactive Route Change - Support Changes(Count)',
#        'Negative Margin Changes(Count)', 'Negative Margin Cost Saving $',
#        'Filter cost saving $']

df = pd.read_excel('Cost Saving1.xlsx')
# print(df.columns)
x= 'Proactive - Cost Saving  $'
y= 'Proactive - Cost Saving Changes(Count)'
a=' Negative Margin Cost Saving $'
b= 'Negative Margin Changes(Count)'
c= 'Proactive Quality Improvement Changes(Count)'
d= 'Filter cost saving $'
sns.relplot(x=x,y=y,data=df, kind= 'line')
# sns.relplot(x=a,y=b,data=df, kind= 'line')
sns.relplot(x=c,y=d,data=df, kind= 'line')


plt.show()