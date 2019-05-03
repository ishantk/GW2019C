file = open("students.csv", "r")
data = file.read()
print(data)

print("******")

data = file.read()
print(data)

# Release Memory Resources
file.close()