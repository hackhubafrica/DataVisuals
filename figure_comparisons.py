import matplotlib.pyplot as plt

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
steps_walked = [8934, 14902, 3409, 25672, 12300, 2023, 6824]
steps_last_week = [9788, 8710, 5308, 17630, 21309, 4002,23232]

#Creating Subplots
#fig, axs[0][0] = plt.subplots()

fig, axs= plt.subplots(1,2)
''''
# Plot line chart
axs[0].plot(days, steps_walked, "o-g")
axs[0].plot(days, steps_last_week, "v--m")
axs[0].set_title("Step count | This week and last week")
axs[0].set_xlabel("Days of the week")
axs[0].set_ylabel("Steps walked")
axs[0].grid(True)
axs[0].legend(["This week", "Last week"])

'''

# Plot bar chart
axs[1].bar(days, steps_walked)
axs[1].bar(days, steps_last_week)
axs[1].set_title("Step count | This week and last week")
axs[1].set_xlabel("Days of the week")
axs[1].set_ylabel("Steps walked")
axs[1].grid(True)

plt.show()

