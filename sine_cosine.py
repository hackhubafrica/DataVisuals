import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Plot using the custom plot function with additional kwargs
plt.plot(x, y1, linestyle='-', color='blue', label='Sine')
plt.plot(x, y2, linestyle='--', color='red', label='Cosine')

# Adding labels and title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine and Cosine Waves')
plt.legend()

# Show plot
plt.show()
