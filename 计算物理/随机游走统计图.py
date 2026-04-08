#random walk
#author@wfli

import numpy as np
import matplotlib.pyplot as pl
import random
from scipy.optimize import leastsq

nwalker = 50000; nstep = 100

time = np.arange(nstep)
ree = np.zeros(nwalker, dtype=float)
r2_ave = np.zeros(nstep, dtype=float) # mean square distance
y_fit = np.zeros(nstep, dtype=float)
p0 = np.zeros(2, dtype=float)

for iwalk in range(nwalker):
    random.seed(None)
    x = 0.0; y = 0.0

    for istep in range(nstep):
        theta = random.random()*2*3.1415927
        dx = np.cos(theta); dy = np.sin(theta)
        x = x + dx; y = y + dy
        r2 = x**2 + y**2
        r2_ave[istep] = r2_ave[istep] + r2/nwalker

    ree[iwalk] = np.sqrt(x**2+y**2)

rprob, redge = np.histogram(ree,bins=20)
dist = 0.5*(redge[0:-1]+redge[1:])
rprob_density = rprob/(2*3.1415927*dist)

def func(x, p):
    a0 = p[0]
    alpha0 = p[1]
    return a0*pow(x,alpha0)

def residuals(p, y ,x):
    return y - func(x, p)

p0[0] = 1.0; p0[1] = 1.0
parameters = leastsq(residuals, p0, args=(time,r2_ave))
for i in np.arange(nstep):
    y_fit[i] = parameters[0][0]*np.power(time[i],parameters[0][1])

fig = pl.figure(figsize=(10,3))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

pl.subplots_adjust(left=0.15,bottom=0.1,top=0.9,right=0.95,\
hspace=0.25,wspace=0.3)

ax1.plot(time[::3],r2_ave[::3],'ro',fillstyle='none',lw=1.0,label='data')
ax1.plot(time,y_fit,'b-',linewidth=2.0,label='fitting')
ax2.plot(dist,rprob,'m-',linewidth=2.0)
ax3.plot(dist,rprob_density,'m-',linewidth=2.0)

ax1.set_xlabel('time',fontsize=15)
ax1.set_ylabel(r'$<R^2>$',fontsize=15)
ax2.set_xlabel('Ree',fontsize=15)
ax2.set_ylabel('distribution',fontsize=15)
ax3.set_xlabel('Ree',fontsize=15)
ax3.set_ylabel('Prob density',fontsize=15)

ax1.legend(loc='upper left',fontsize=15)
pl.show()