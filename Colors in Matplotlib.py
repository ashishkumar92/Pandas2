# import matplotlib.pyplot as plt
# import pandas as pd
# import re
# index=['python','pandas','spark','powerbi','ml']
# l = ["Digits_T4790722T","Digits_T4853997T","Digits_T4853997T"]
# days=[10,5,2,7,8]
# co=['RED','YELLOW','GREEN','BLUE','ORANGE']
# plt.pie(days,labels=index,autopct='%1.1f%%',colors=co)
# plt.title("DS Training")
# plt.show()
# p = " ^[A-Z]{6}[\\_]"
# t = re.search('%s(.*)%s' %("T","T"),)
# p = " ".join(str(e) for e in l )
# t= list(filter(p.startswith,"T")) != []
# filename = " ".join(str(e) for e in l )
# for i in l:
#     a=i.startswith('Digits_') and i.endswith('T')
#     a=i.replace('Digits_', '').replace('T', '')
#     print (a)
# res = []
# [res.append(x) for x in test_list if x not in res]
# print([k.append(x) for x in l if x not in l])

# from tqdm import tqdm
# import time
#
# for i in tqdm(range(1001),
#               desc="Loading…",
#               ascii=False, ncols=75):
#     time.sleep(0.01)
#
# print("Complete.")

import tkinter as tk
from tkinter import ttk

# root window
root = tk.Tk()
root.geometry('300x120')
root.title('Progressbar Demo')

root.grid()

# progressbar
pb = ttk.Progressbar(
    root,
    orient='horizontal',
    mode='indeterminate',
    length=280
)
# place the progressbar
pb.grid(column=0, row=0, columnspan=2, padx=10, pady=20)


# start button
start_button = ttk.Button(
    root,
    text='Start',
    command=pb.start
)
start_button.grid(column=0, row=1, padx=10, pady=10, sticky=tk.E)

# stop button
# stop_button = ttk.Button(
#     root,
#     text='Stop',
#     command=pb.stop
# )
# stop_button.grid(column=1, row=1, padx=10, pady=10, sticky=tk.W)


root.mainloop()