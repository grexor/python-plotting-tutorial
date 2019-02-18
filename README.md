# python-plotting-tutorial
Short tutorial on python plotting (3h)

matplotlib 3.0.2
----------------

### About matplotlib

The project was initiated by John D. Hunter in 2008. The initial introductory text stated:

<p align="justify">"Matplotlib is a library for making 2D plots of arrays in Python. Although it has its origins in emulating the MATLAB graphics commands, it is independent of MATLAB, and can be used in a Pythonic, object oriented way. Although Matplotlib is written primarily in pure Python, it makes heavy use of NumPy and other extension code to provide good performance even for large arrays."</p>

To keep in mind: "**Matplotlib tries to make easy things easy and hard things possible**". The matplotlib "easy" part is named **pyplot** module and provides a MATLAB-like interface.

![From matplotlib.org](https://matplotlib.org/_images/anatomy.png "matplotlib parts of a figure, from matplotlib.org")

### Example 1

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

### Exercise 1

Modify the code from Example 1 to plot tan(x) on the range of -10 .. 10, with the step of 0.1. Your points will be -10, -9.9, -9.8 .. 9.9, 10. Also, don't plot a continuous line (plot), but only plot points (scatter). Color the points red (#FF0000).

<details>
<summary>Solution</summary>
  
```python
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

t = np.arange(-10, 10.0, 0.1) # Data for plotting
s = np.tan(t)

fig, ax = plt.subplots()
ax.scatter(t, s, c="#FF0000") # c="red" would also work

ax.set(xlabel='x range', ylabel='tan(x)', title='tan(x) on range -10..10 [step 0.1]')
ax.grid()

fig.savefig("exercise1.pdf")
plt.show()
```

</details>

plotly
------
