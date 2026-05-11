import numpy as np
import pylab as pl

n = 1000
omega0_sq = 1.0
kappa_sq = 0.5

a = np.zeros([n, n])
for i in range(n):
    for j in range(n):
        if i == j:
            a[i, j] = omega0_sq + 2.0 * kappa_sq
        if i == j + 1 or j == i + 1:
            a[i, j] = -kappa_sq


eigenValues, eigenVectors = np.linalg.eigh(a)
idx = eigenValues.argsort()
eigenValues = eigenValues[idx]
eigenVectors = eigenVectors[:, idx]

print(eigenValues)
print(eigenVectors)

index = np.arange(n)
fig = pl.figure(figsize=(12, 4))
ax1 = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax1.plot(index, eigenValues, 'ro', label='mode')
ax1.set_xlabel(r'mode id', fontsize=20)
ax1.set_ylabel(r'frequence', fontsize=20)


ax2.plot(index, eigenVectors.T[5,:], 'r-', label='mode')
ax2.set_xlabel(r'position', fontsize=20)
ax2.set_ylabel(r'amplitude', fontsize=20)

pl.subplots_adjust(left=0.15, bottom=0.1, top=0.9, right=0.95,
                   hspace=0.25, wspace=0.3)
pl.show()