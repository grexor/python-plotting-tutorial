import matplotlib
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(42)

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

fig.tight_layout() # good trick
plt.show()
