# python-plotting-tutorial

Short tutorial (1.5h) on python plotting with [matplotlib](http://www.matplotlib.org)

### Contents of tutorial

- [About matplotlib](#matplotlib)
- [Example 1: simple plot](#example1)
- [Example 2: histogram](#example2)
- [Example 3: coloring areas between plots](#example3)
- [Summary and take home message](#summary)

matplotlib 3.0.2
----------------

<a name="matplotlib"></a>
### About matplotlib

The project was initiated by John D. Hunter in 2008. The initial introductory text stated:

<p align="justify">"Matplotlib is a library for making 2D plots of arrays in Python. Although it has its origins in emulating the MATLAB graphics commands, it is independent of MATLAB, and can be used in a Pythonic, object oriented way. Although Matplotlib is written primarily in pure Python, it makes heavy use of NumPy and other extension code to provide good performance even for large arrays."</p>

To keep in mind: "**Matplotlib tries to make easy things easy and hard things possible**". The matplotlib "easy" part is named **pyplot** module and provides a MATLAB-like interface.

<img src="https://matplotlib.org/_images/anatomy.png" width=600>

<a name="example1"></a>
### Example 1: simple basic plot

We start with this basic example of plotting 1+sin(x) on range 0..2:

```python
import matplotlib
# matplotlib.use('Agg') # use this backend if you would just like to save images/figures to files (PNG, JPG, PDF)
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

Modify the code from Example 1 to plot tan(x) on the range of -10 .. 10, with the step of 0.1. Your points will be -10, -9.9, -9.8 .. 9.9, 10. Also, don't plot a continuous line (plot), but only plot points (scatter). Color the points red (#FF0000). Save figure to PDF file.

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

Let's try to style this plot and make it more compact. With help of [matplotlib documentation](https://matplotlib.org/api/matplotlib_configuration_api.html#matplotlib.rc) do the following:

* change font size of axis labels and title to 8px
* display the grid and make it more transparent (alpha=0.2), check Example 1 to see how to display the grid
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

Our last example introduces the final exercise. Imagine we have 2 plots on the same figure:

```python
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

plt.legend() # show legend

fig.savefig("example3.png")
plt.show()
```

The first plot (x, y1) is of the function 1+x+x^2, the second plot (x, y2) is of the function -4+5x+x^2+x^3. Run the code and move on to the exercise to learn additional styling and how to color areas between plots.

#### Exercise 3

Again using hints from this text and [matplotlib documentation](https://matplotlib.org/api/matplotlib_configuration_api.html#matplotlib.rc), modify the above Example 3 code to include:

* add legends to the two plots (hint: use attribute `legend` with the plot command); finally, you have to display the legend (`plt.legend`)
* make the two plots red and blue (use the attribute `c` of `.plot`); you can also use pastel colors, like #ff6961 for red and #779ecb for blue
* make lines of the two plots thicker; use `linewidth` attribute of the plot method
* color the area in-between the plots with a light gray (#dddddd or similar) color; hint: try using `fill_between`
* set x-axis and y-axis limits to some reasonable value, so the labels on the sides of the axis are displayed nicely; an example could be -5..20 (y), -0.2..2.2 (x); use `set_xlim` and `set_ylim`

<details>
<summary>Solution</summary>

```python
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
```

</details>

<a name="summary"></a>
### Summary and take home message

Basic plotting with matplotlib is easy however fine-tuning your plots requires some additional work. Overall, matplotlib is a very powerful tool to produce high-quality plots that we can customize in great detail.

#### Quick start summary

* first 3 steps:
```python
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
```
* you can start plotting immediatelly:
```python
fig, ax = plt.subplots()
x = np.arange(0.0, 2.0, 0.01)
y = 2*x
ax.plot(x, y)
plt.show()
```
* easily style the `ax.plot` with several attributes
  * `c="red"` or `c="#FF0000"`
  * `linewidth=2` (or any integer)
  * `label="my plot label"`: this is then recognized by `plt.legend()`
* other useful commands
  * `plt.grid(alpha=1)`: shows the grid
  * `ax.set_ylim(y_from, y_to)` and `ax.set_xlim(x_from, x_to)`: set the display limits
  * `ax.fill_between(x, y1, y2, color="lightgray")`: fills the area between y1 and y2 with light gray color
  * `plt.tight_layout()`: usuful to make the figure nicer
  * `fig.savefig(filename)`: save figure to file, supported formats: png, jpg, svg, pdf (simply change the file extension)
  
Hope you enjoyed the tutorial, please [open an issue](https://github.com/grexor/python-plotting-tutorial/issues) if you have further comments.
