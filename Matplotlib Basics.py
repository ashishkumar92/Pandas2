import matplotlib.pyplot as plt

name = ['nihal','rahul','puneet','kanchan','vinod','divyanshu']
over1 = [15,30,36,25,10,5]
over2 = [25,15,10,25,20,36]
plt.plot(name,over1,label='Over 1')
plt.plot(name,over2,label='Over 2')
plt.legend() # legend is used to activate label.
plt.grid()  # grid is used for graph paper .
plt.title('game')
plt.xlabel('Names')
plt.ylabel('Runs')
plt.show()