import random
import time
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import csv
import time

plt.style.use('fivethirtyeight')

# x_vals = [0,1,2,3,4,5,1,2,3,4,4,5,6,6,7,5,3,3,1,12,33,21,2,3,4,21,3,4,5,6,7,8,5,54,3,2,2,5,1,2,3,4,4,5,6,6,7,5,3,3]
# y_vals = [0,1,3,2,3,5,5,1,2,3,4,4,5,6,6,7,5,3,3,5,1,2,3,4,4,5,6,6,7,5,3,3,5,1,2,3,4,4,5,6,6,7,5,3,3,5,1,2,3,4]
x_vals = []
y_vals = []

index = count()

def animate(i):
    x_vals.append(time.strftime('%Y-%m-%d %H:%M:%S'))
    y_vals.append(random.randint(0,5))
    plt.xticks(rotation=90)
    plt.plot(x_vals,y_vals)
# Open the CSV file for writing
# with open('live_data.csv', 'w', newline='') as file:
#     writer = csv.writer(file)
#
#     # Write the header row
#     writer.writerow(['Timestamp', 'Value'])
#     t=[]
#     # Main data recording loop
#     i=0
#     while i<50:
#         # Simulate getting live data from a sensor
#         timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
#         value = y_vals.append(random.randint(0,5))

        # Write data to CSV file
        # writer.writerow([timestamp, value])
        # print(i)
        # Wait for a specific interval (e.g., 1 second)
        # time.sleep(1)
        # i+=1
ani = FuncAnimation(plt.gcf(),animate,frames=10,interval=1000)

plt.plot(x_vals,y_vals)
plt.tight_layout()
plt.show()




