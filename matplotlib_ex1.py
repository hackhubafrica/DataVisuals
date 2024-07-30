#Matplotlib is the whole package and matplotlib.pyplot is a module in Matplotlib

import matplotlib.pyplot as plt
import numpy as np
import pandas

'''
fig = plt.figure() # an empty figure with no axes
fig.suptitle('No axes on this figure') # Add a title so we know which it is
fig, ax_lst = plt.subplots(2, 2) # a figure with a 2x2 grid of Axes
'''


a = pandas.DataFrame(np.random.rand(4,5), columns = list('abcde'))
a_asarray = a.values
print(type(a))
print('a is equal to',a)

print(type(a_asarray))
print('a_asarray is equal to ',a_asarray)
#and to convert a np.matrix
b = np.matrix([[1,2],[3,4]])
b_asarray = np.asarray(b)


print(type(b))
print('b is equal to',b)

print(type(b_asarray))
print('b_asarray is equal to',b_asarray)
#print(b)
#print(b_asarray)



x = np.linspace(0, 2, 100)
plt.plot(x, x, label='linear')
plt.plot(x, x**2, label='quadratic')
plt.plot(x, x**3, label='cubic')
#plt.plot(x, np.expx, label='exponential')
plt.xlabel('x label')
plt.ylabel('y label')
plt.title("Simple Plot")
plt.legend()
plt.show()