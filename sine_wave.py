import matplotlib.pyplot as plt
import numpy as np

#x = np.arange(0, 10, 0.2)
x = np.linspace(0, 10, 100)
y = np.sin(x)
fig, ax = plt.subplots()
ax.plot(x, y)

'''
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
plt.plot(x, y1, linestyle='-', color='blue', label='Sine')
'''



def my_plotter(ax, data1, data2, param_dict):
    out = ax.plot(data1, data2, **param_dict)
    return out
# which you would then use as:
data1, data2, data3, data4 = np.random.randn(4, 100)
fig, ax = plt.subplots(1, 1)
my_plotter(ax, data1, data2, {'marker': 'x'})

plt.show()