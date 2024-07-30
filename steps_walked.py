import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps_walked = [8934, 14902, 3409, 25672, 12300, 2023, 68]
steps_last_week = [9788, 8710, 5308, 17630, 21309, 4002,3223]
#You can call plot() with two input arguments instead of one to determine whatdata to use for both the x– and y-axes
plt.plot(days,steps_walked,"o:r")
plt.plot(days, steps_last_week,"v--g")
  
'''
: draws dotted lines
o shows that the marker should be the o symbol
x shows that the marker should be the x symbol
- draws the line
r indicates the colour should be red
'''

#You can explore a few more functions in matplotlib.pyplot to add titles and labels to the plot
plt.title("Step count for the week")
plt.xlabel("Days of the week")
plt.ylabel("Steps walked")
plt.grid(True)
plt.show()
