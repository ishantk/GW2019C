import matplotlib.pyplot as plt

jobs = [120, 80, 60]
domains = ["IT", "Marketing", "Accounts"]

plt.pie(jobs, labels=domains)
plt.legend()
plt.show()