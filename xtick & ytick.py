import matplotlib.pyplot as plt
import numpy as np
name = ['nihal','rahul','puneet','kanchan','vinod','divyanshu']
over1 = [15,30,36,25,10,5]
over2 = [25,15,10,25,20,36]
#
# j = [1,2,3,4,5,6]
j = range(1,7)
# k = [1.2,2.2,3.2,4.2,5.2,6.2]
k = np.arange(1.3,7.3,1)    #range doesn't take float value.
plt.bar(j,over1,width=0.3)
# plt.bar(k,over2,width=0.3)
plt.xticks(j,name)
# plt.yticks(over2,j)


sal1 = [15000,30000,36000,25000,14000,50000]
sal2 = [25000,15000,10000,25000,20000,36000]
plt.plot(sal1,sal2)
plt.xticks([1000, 10000, 100000],['1k', '10k', '100k'])



plt.show()