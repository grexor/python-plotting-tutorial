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

x = np.arange(0.0, 2.0, 0.01) # data for plotting

y1 = 1+x+x*x
ax.plot(x, y1, c='#ff6961', label="1+x+x^2", linewidth=2)
y2 = -4+5*x+x*x+x*x*x
ax.plot(x, y2, c='#779ecb', label="-4+5x^2+x^3", linewidth=2)

ax.fill_between(x, y1, y2, color='#dddddd') # fill the space in-between the plots

ax.set(xlabel='x in range 0..2 by steps of 0.01', ylabel='', title='plot coloring example')
ax.set_ylim(-5, 20) # set area to display (y-axis)
ax.set_xlim(-0.2, 2.2) # set area to display (x-axis)
plt.grid(alpha=0.2)

plt.legend() # show legend

fig.savefig("example3.png")
plt.show()
