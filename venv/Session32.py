# import matplotlib as mat
# print(mat.__version__)

import matplotlib.pyplot as plt

# Y = f(X)

# Y = [5, 7, 9, 11, 13]
# We consider X is indexes !!

# plt.plot(Y)
# plt.show()

"""
X = list(range(10))
Y = [n*n for n in X]

print(X)
print(Y)

plt.plot(X, Y)
plt.show()
"""

X = list(range(10))
Y1 = [n for n in X]
Y2 = [n*n for n in X]
Y3 = [n*n*n for n in X]

plt.plot(X, Y1, label="Y1")
plt.plot(X, Y2, label="Y2")
plt.plot(X, Y3, label="Y3")

plt.legend()

plt.xlabel("X-Axis")
plt.ylabel("Y-Axis")
plt.title("Polynomial Graphs")

plt.xlim(0, 10)
plt.ylim(0, 1000)

plt.grid(True)

plt.savefig("MyPlot.png")

plt.show()

# Assignment : Represent CityTemps.csv on Graph
# Explore : https://matplotlib.org/tutorials/index.html




