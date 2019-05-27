import numpy as np
data = np.genfromtxt("CityTemps.csv", delimiter=",")
print(data)
print(data.shape)
print(data[1][2])

np.savetxt("CityTemps1.csv", data, delimiter=",")
print(">> File Saved")

# City with Highest Temperature and when (Year and Month)
# City with Lowest Temperature and when (Year and Month)

# City which is Hottest
# City which is Coldest