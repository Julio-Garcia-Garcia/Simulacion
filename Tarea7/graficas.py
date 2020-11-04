import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.ticker import LinearLocator
import numpy as np
import math as ma

fig=plt.figure()
ax= Axes3D(fig)

x=np.linspace(-1,0.5,20)
y=np.linspace(-1,0.5,20)
X, Y =np.meshgrid(x,y)

def z(x,y):
    return (np.sin(1000 * x * y) * ((x + 0.5) ** 4 - 30 * x ** 2 - 20 * x + (y + 0.5) ** 4 - 30 * y ** 2 - 20 * y) / 100)


ax.plot_surface(X, Y, z(X,Y),cstride=1,rstride=1)
ax.set_xlabel('$x$', fontsize=10, rotation=150)
ax.set_ylabel('$y$', fontsize=10)
ax.set_zlabel('$z$', fontsize=10)

plt.show()