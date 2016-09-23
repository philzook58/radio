import numpy as np
import sys
import matplotlib.pyplot as plt


filename = sys.argv[1]
backfile = sys.argv[2]


freq, db = np.loadtxt(filename, delimiter=',', usecols=(0, 1), unpack=True)
backfreq, backdb = np.loadtxt(backfile, delimiter=',', usecols=(0, 1), unpack=True)

plt.plot(freq,db-backdb)
plt.xlabel('Hz')
plt.ylabel('db')
plt.show()
