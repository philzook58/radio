import numpy as np
import sys
import matplotlib.pyplot as plt


filename = sys.argv[1]


freq, db = np.loadtxt(filename, delimiter=',', usecols=(0, 1), unpack=True)

plt.plot(freq,db)
plt.xlabel('Hz')
plt.ylabel('db')
plt.show()
