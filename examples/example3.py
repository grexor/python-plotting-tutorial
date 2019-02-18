import matplotlib
import matplotlib.pyplot as plt
import numpy as np
font_size = 8
matplotlib.rcParams['axes.labelsize'] = font_size
matplotlib.rcParams['axes.titlesize'] = font_size
matplotlib.rcParams['xtick.labelsize'] = font_size
matplotlib.rcParams['ytick.labelsize'] = font_size
matplotlib.rcParams['legend.fontsize'] = font_size
matplotlib.rc('axes',edgecolor='gray')
matplotlib.rcParams['axes.linewidth'] = 0.2
matplotlib.rcParams['legend.frameon'] = 'False'

fig, ax = plt.subplots()

x = np.arange(0.0, 2.0, 0.01) # Data for plotting

y1 = 1+x+x*x
ax.plot(x, y1)
y2 = -4+5*x+x*x+x*x*x
ax.plot(x, y2)

ax.set(xlabel='x in range 0..2 by steps of 0.01', ylabel='', title='plot coloring example')
plt.grid(alpha=0.2)

fig.savefig("example3.png")
plt.show()
