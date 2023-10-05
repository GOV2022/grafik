import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure(2)
ax = fig.add_subplot(111,projection='3d')
x = np.linspace(-5, 5, 30)
y = np.linspace(-5, 5, 30)
x, y = np.meshgrid(x,y)
z = x * np.sin(y) + np.sin(x) * y
ax.plot_surface(x, y, z, color = 'limegreen')
plt.show()
#
