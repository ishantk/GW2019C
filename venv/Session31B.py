import pandas as pd

s1 = pd.Series([10, 20, 30, 40, 50])
print(s1)

ages = {"john":30, "fionna":20, "kia":22, "Leo":24, "Becca":22}
s2 = pd.Series(ages)
print(s2)

# Access Element
print(s1[0])
print(s2["kia"])

# Slicing the Elements:
print(s1[1:])
print(s1[:2])
print(s1[2:5])

print(s2["fionna": ])
print(s2["fionna": "Leo"])

