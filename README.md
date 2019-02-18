# python-plotting-tutorial

Short tutorial (1.5h) on python plotting with [matplotlib](http://www.matplotlib.org)

### Contents of tutorial

- [About matplotlib](#matplotlib)
- [Example 1: simple plot](#example1)
- [Example 2: histogram](#example2)
- [Example 3: coloring areas between plots](#example3)

matplotlib 3.0.2
----------------

<a name="matplotlib"></a>
### About matplotlib

The project was initiated by John D. Hunter in 2008. The initial introductory text stated:

<p align="justify">"Matplotlib is a library for making 2D plots of arrays in Python. Although it has its origins in emulating the MATLAB graphics commands, it is independent of MATLAB, and can be used in a Pythonic, object oriented way. Although Matplotlib is written primarily in pure Python, it makes heavy use of NumPy and other extension code to provide good performance even for large arrays."</p>

To keep in mind: "**Matplotlib tries to make easy things easy and hard things possible**". The matplotlib "easy" part is named **pyplot** module and provides a MATLAB-like interface.

![From matplotlib.org](https://matplotlib.org/_images/anatomy.png "matplotlib parts of a figure, from matplotlib.org")

<a name="example1"></a>
### Example 1: simple basic plot

We start with this basic example of plotting 1+sin(x) on range 0..2:

```python
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

x = np.arange(0.0, 2.0, 0.01) # data for plotting
y = 1 + np.sin(x)

fig, ax = plt.subplots() # get figure in fig and axis in ax object
ax.plot(x, y)

ax.set(xlabel='time (s)', ylabel='1+sin(x)', title='basic matplotlib example') # set xlabel, ylabel and title
ax.grid()

fig.savefig("example1.png") # save figure
plt.show() # show figure
```

Notice the figure is saved to **example1.png** using `.savefig()` and displayed with `show()`.

#### Exercise 1

Modify the code from Example 1 to plot tan(x) on the range of -10 .. 10, with the step of 0.1. Your points will be -10, -9.9, -9.8 .. 9.9, 10. Also, don't plot a continuous line (plot), but only plot points (scatter). Color the points red (#FF0000).

<details>
<summary>Solution</summary>
  
```python
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-10, 10.0, 0.1) # data for plotting
s = np.tan(t)

fig, ax = plt.subplots()
ax.scatter(t, s, c="#FF0000") # c="red" would also work

ax.set(xlabel='x range', ylabel='tan(x)', title='tan(x) on range -10..10 [step 0.1]')
ax.grid()

fig.savefig("exercise1.pdf") # save to PDF simply by changing filename extension (.pdf)
plt.show()
```

</details>

<a name="example2"></a>
### Example 2: histogram

A slightly more complex example with a histogram:

```python
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

fig.tight_layout() # make display nicer
plt.show()
```

#### Exercise 2

Let's try to style this plot and make it more compact. Try to do the following:

* change font size of axis and title to 8px (check [matplotlib documentation](https://matplotlib.org/api/matplotlib_configuration_api.html#matplotlib.rc) on how to change font sizes)
* display the grid and make it more transparent (alpha 0.2)
* save the plot to a SVG file
* try out `tight_layout()`

<details>
<summary>Solution</summary>

```python
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
```

</details>

<a name="example3"></a>
### Example 3: coloring areas between plots
