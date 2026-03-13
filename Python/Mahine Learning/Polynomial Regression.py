import sys
import matplotlib
matplotlib.use('Qt5Agg')

import matplotlib.pyplot as plt

x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28]
y = [100, 98, 96, 94, 92, 90, 88, 89, 90, 92, 94, 96, 98, 100]

plt.scatter(x, y)
plt.show()

plt.savefig(sys.stdout.buffer)
sys.stdout.flush()
