import numpy as np
filename = 'TRADES.20180227.csv'
data = np.loadtxt(filename, delimiter=',', dtype=str)
print(data)
