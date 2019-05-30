import matplotlib.pyplot as plt

X = [1, 2, 3, 4, 5]

Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]

# plt.plot(X, Y1, "y")
# plt.plot(X, Y2, "m")
# plt.plot(X, Y3, "b")

# plt.plot(X, Y1, "--")
# plt.plot(X, Y2, "-.")
# plt.plot(X, Y3, ":")

plt.plot(X, Y1, "o")
plt.plot(X, Y2, "^")
plt.plot(X, Y3, "D")

plt.show()

# Please Explore More Graphs : https://matplotlib.org/tutorials/index.html
# BoxPlot : https://matplotlib.org/3.1.0/gallery/pyplots/boxplot_demo_pyplot.html#sphx-glr-gallery-pyplots-boxplot-demo-pyplot-py
# Seaborn : https://seaborn.pydata.org/
# Explore Basic Relational Graphs : https://seaborn.pydata.org/tutorial/relational.html
# Graphical Visualization of CityTemps.csv in Matplotlib / Seaborn
