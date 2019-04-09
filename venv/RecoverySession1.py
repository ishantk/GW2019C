# Creating a Single Value Container
# 20 is data
age = 20
print("Wow!! HashCode of age is:",id(age)) # id(age)

# Update Data
age = 30
print("HashCode of age after update is:",id(age))

age = age // 3

# Read Data in Container
print("age is:",age)
print("HashCode of age after update is:",id(age))

# Multi Value Container
ages = 10, 20, 30, 40, 50
print("ages is: ",ages)
print("HashCode of ages is:",id(ages))

print(type(age))
print(type(ages))