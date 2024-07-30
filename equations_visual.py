#static plots into dynamic animations. You’ll use the following equation for this exercise:
#z = sin(x^2 + y^2 - a )

import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-5, 5, 1000)
y = np.linspace(-5, 5, 1000)

X, Y = np.meshgrid(x, y)

fig, ax = plt.subplots()

a = 30
Z = np.sin(X ** 2 + Y ** 2 - a)

ax.imshow(Z)
plt.show()
