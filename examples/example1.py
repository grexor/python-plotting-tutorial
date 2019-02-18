import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 2.0, 0.01) # data for plotting
y = 1 + np.sin(x)

fig, ax = plt.subplots()
ax.plot(x, y)

ax.set(xlabel='time (s)', ylabel='1+sin(x)', title='basic matplotlib example')
ax.grid()

fig.savefig("example1.png")
plt.show()
