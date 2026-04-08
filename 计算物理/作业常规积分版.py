import numpy as np
import matplotlib.pyplot as pl
from scipy.special import roots_legendre


R = 1.0
Q = 1.0

N = 107


potential = []
x0 = np.arange(0,1,1/N)


def U(x, y):
    phi = 0.0
    for i in range(N):
        theta = 2 * np.pi * x0[i]
        xr = R * np.cos(theta)
        yr = R * np.sin(theta)
        dist = np.sqrt( (x-xr) **2 + (y-yr) **2)
        phi += 0.5 / (dist * N)
    return  phi


xaxis = np.arange(-3.0,3.0,0.1)
yaxis = np.arange(-3.0,3.0,0.1)

for x_0 in xaxis:
    for y_0 in yaxis:
        potential.append( U(x_0,y_0) )



apotential = np.array(potential)
apotential.shape = len(xaxis) , len(yaxis)
apotential_T = apotential.T

fig = pl.figure(figsize=(15,7))
ax1 = fig.add_subplot(1,2,1)
levels = np.arange(0.0,5.0,0.1)
extent = [-3.0, 3.0, -3.0, 3.0]
cs = ax1.contourf(apotential_T,levels,origin='lower',extent=extent,cmap=pl.cm.rainbow)



ax1.set_xlabel('X',size=20)
ax1.set_ylabel('Y',size=20)
ax1.set_xlim(-3.0, 3.0)
ax1.set_ylim(-3.0, 3.0)
ax1.set_title('Potential',size=20)
pl.show()