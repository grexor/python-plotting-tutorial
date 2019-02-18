import matplotlib
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)

font_size = 8
matplotlib.rcParams['axes.labelsize'] = font_size
matplotlib.rcParams['axes.titlesize'] = font_size
matplotlib.rcParams['xtick.labelsize'] = font_size
matplotlib.rcParams['ytick.labelsize'] = font_size
matplotlib.rcParams['legend.fontsize'] = font_size
matplotlib.rc('axes',edgecolor='gray')
matplotlib.rcParams['axes.linewidth'] = 0.2
matplotlib.rcParams['legend.frameon'] = 'False'
import matplotlib.colors as mcolors

mu = 100  # mean of distribution
sigma = 15  # standard deviation of distribution
x = mu + sigma * np.random.randn(5000)
num_bins = 50

fig, ax = plt.subplots()
n, bins, patches = ax.hist(x, num_bins, density=1) # plot histogram

# add 'best fit' line
y = ((1 / (np.sqrt(2 * np.pi) * sigma)) * np.exp(-0.5 * (1 / sigma * (bins - mu))**2))
ax.plot(bins, y, '--')
ax.set_xlabel('histogram bins')
ax.set_ylabel('probability density')
ax.set_title(r'histogram: $\mu=100$, $\sigma=15$')

plt.grid()
plt.grid(alpha=0.2)

fig.tight_layout() # good trick
fig.savefig("exercise2.svg")
plt.show()
