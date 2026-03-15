import numpy as np
import matplotlib.pylab as pl
import random
# import sys

outfile = open("walk-tra.dat","w")

line = input("input the maximal number of walk steps:")
nstep = int(line)
print("the maximal number of walk steps is:",nstep)

if nstep > 1000:
    print("too many steps")
    exit()
elif nstep < 50:
    print("too few steps")
    exit()

xlist = []
ylist = []
x = 0.0
y = 0.0
xlist.append(x)
ylist.append(y)

random.seed(None)
for i in range(0,nstep):
    theta = random.random() * 2.0 * np.pi
    dx = np.cos(theta)
    dy = np.sin(theta)
    x += dx
    y += dy
    outfile.write("%d\t%0.2f\t%0.2f\n" % (i,x,y))
    # xlist.append(x)
    # ylist.append(y)

outfile.close()

# pl.plot(xlist,ylist,"r-",lw=2)
# pl.show()
