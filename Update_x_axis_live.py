#
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
# import numpy as np
# # %matplotlib notebook
#
# #data generator
# data = np.random.random((100,))
#
# #setup figure
# fig = plt.figure(figsize=(5,4))
# ax = fig.add_subplot(1,1,1)
#
# #rolling window size
# repeat_length = 25
#
# ax.set_xlim([0,repeat_length])
# ax.set_ylim([-2,2])
#
#
# #set figure to be modified
# im, = ax.plot([], [])
#
# def func(n):
#     im.set_xdata(np.arange(n))
#     im.set_ydata(data[0:n])
#     if n>repeat_length:
#         lim = ax.set_xlim(n-repeat_length, n)
#     else:
#         lim = ax.set_xlim(0,repeat_length)
#     return im
#
# ani = animation.FuncAnimation(fig, func, frames=data.shape[0], interval=30, blit=False)
#
# plt.show()
#
# #ani.save('animation.gif',writer='pillow', fps=30)
#
# import numpy as np
# from matplotlib import pyplot as plt
# from matplotlib import animation
#
# # First set up the figure, the axis, and the plot element we want to animate
# fig = plt.figure()
# ax = plt.axes(xlim=(0, 2), ylim=(-2, 2))
# line, = ax.plot([], [], lw=2)
#
# # initialization function: plot the background of each frame
# def init():
#     line.set_data([], [])
#     return line,
#
# # animation function.  This is called sequentially
# def animate(i):
#     x = np.linspace(0, 2, 1000)
#     y = np.sin(2 * np.pi * (x - 0.01 * i))
#     line.set_data(x, y)
#     # plt.xlim(right=3)  # adjust the right leaving left unchanged
#     plt.xlim(left=1)  # adjust the left leaving right unchanged
#     return line,
#
# # call the animator.  blit=True means only re-draw the parts that have changed.
# anim = animation.FuncAnimation(fig, animate, init_func=init,
#                                frames=200, interval=20, blit=True)
#
# plt.show()

import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
# import tmp102
import random
# Create figure for plotting
fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
xs = []
ys = []

# Initialize communication with TMP102
# tmp102.init()

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    # Read temperature (Celsius) from TMP102
    # temp_c = round(tmp102.read_temp(), 2)
    temp_c = random.randint(0,5)

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
    ys.append(temp_c)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    plt.title('TMP102 Temperature over Time')
    plt.ylabel('Temperature (deg C)')

# Set up plot to call animate() function periodically
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
plt.show()