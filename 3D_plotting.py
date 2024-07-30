import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-10, 10, 1000)
y = np.linspace(-10, 10, 1000)

X, Y = np.meshgrid(x, y)

# Handling division by zero
Z = (np.sin(X) / np.where(X == 0, 1, X)) * (np.sin(Y) / np.where(Y == 0, 1, Y))

fig, ax = plt.subplots(subplot_kw={'projection': "3d"})
ax.plot_surface(X, Y, Z, cmap="viridis")

plt.show()
