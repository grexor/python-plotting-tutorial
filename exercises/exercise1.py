import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-10, 10.0, 0.1) # Data for plotting
s = np.tan(t)

fig, ax = plt.subplots()
ax.scatter(t, s, c="#FF0000")

ax.set(xlabel='x range', ylabel='tan(x)', title='tan(x) on range -10..10 [step 0.1]')
ax.grid()

fig.savefig("exercise1.pdf")
plt.show()
