import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(0.0, 2.0, 0.01) # Data for plotting
s = 1 + np.sin(t)

fig, ax = plt.subplots()
ax.plot(t, s)

ax.set(xlabel='time (s)', ylabel='1+sin(x)', title='basic matplotlib example')
ax.grid()

fig.savefig("example1.png")
plt.show()
