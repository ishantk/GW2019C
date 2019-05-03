file = open("students.csv", "r")
data = file.readlines()
print(data)

print(data[0])
print(data[1])
print(data[2])

# For Each or Enhanced For Loop
# for line in data:
#     print(line)

for i in range(0, len(data)):
    print(data[i])

file.close()