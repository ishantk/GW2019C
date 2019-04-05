# Creating a Single Value Container
# And Writing Data 10 in it
age = 10
# age is a reference variable which will have HashCode for data 10
print("age is:",age)
print("HashCode of age is:",id(age))

# Update Operation
age = 20

# Read Operation
print("age is:",age)
print("HashCode of age is:",id(age))

# Reference Copy
johnsAge = age
print("johnsAge is:",age)
print("HashCode of johnsAge is:",id(age))

# Delete Operation
del age
# print("age is:",age) -> error