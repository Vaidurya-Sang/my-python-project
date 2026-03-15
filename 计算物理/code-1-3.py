import matplotlib.pylab as pl

istep = []
xlist = []
ylist = []

with open("walk-tra.dat","r") as infile:
    for lines in infile:
        words = lines.split()
        istep.append(int(words[0]))
        xlist.append(float(words[1]))
        ylist.append(float(words[2]))

pl.plot(xlist,ylist,"k-",lw=1)
pl.xlabel("x")
pl.ylabel("y")
pl.show()