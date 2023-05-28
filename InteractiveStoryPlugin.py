import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
x = np.linspace(-3, 3, 100)
y = np.linspace(-3, 3, 100)
X, Y = np.meshgrid(x, y)
Z = np.sin(X**2 + Y**2)

# Plot the data with custom contour lines
plt.contour(X, Y, Z, levels=[-0.5, 0, 0.5], colors=['red', 'green', 'blue'], linewidths=[1, 2, 3])
plt.show()