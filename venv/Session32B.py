import numpy as np
import matplotlib.pyplot as plt

"""
A = [1, 2, 3, 4, 5]
B = [10, 20, 30, 40, 50]

plt.bar(A, B)
plt.show()

"""


sales = {"2015":50, "2016":70, "2017":50, "2018":90, "2019":120}

"""
plt.bar(0, sales["2015"])
plt.bar(1, sales["2016"])
plt.bar(2, sales["2017"])
plt.bar(3, sales["2018"])
plt.bar(4, sales["2019"])

plt.show()
"""

for i, key in enumerate(sales):
    # print(i, key)
    # plt.bar(key, sales[key])
    plt.bar(i, sales[key])


X = np.arange(len(sales))
print(X)

plt.xticks(X, sales.keys())
plt.xlabel("Year")
plt.ylabel("Sales")
plt.title("Maruti Sales")

plt.show()