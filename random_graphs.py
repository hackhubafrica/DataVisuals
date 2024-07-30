import matplotlib.pyplot as plt
import numpy as np

#data1, data2, data3, data4 = np.random.randn(4, 100)
data1, data2 = np.random.randn(2, 100)

#A helper function to make a graph
def my_plotter(ax, data1, data2, param_dict):
    out = ax.plot(data1, data2, **param_dict)
    return out

# which you would then use as:
fig, ax = plt.subplots(1, 1)                               
my_plotter(ax, data1, data2, {'marker': 'x'})


#If you wanted to have 2 sub-plots:
'''
fig, (ax1, ax2) = plt.subplots(1, 2)
my_plotter(ax1, data1, data2, {'marker': 'x'})
my_plotter(ax2, data3, data4, {'marker': 'o'})
'''
plt.show()