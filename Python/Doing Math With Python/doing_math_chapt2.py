# Doing Math With Python
# Chapter 2 Visualizing Data With Graphs

import matplotlib.pyplot as plt

list0ne = [1, 2, 3]

for x, y in enumerate(list0ne):
    print(x, y)

x_nums = [1, 2, 3]
y_nums = [4, 5, 6]

plt.plot(x_nums, y_nums)

plt.show()
