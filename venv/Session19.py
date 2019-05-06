"""
number = 203

s = str(number)

print(s[0])
print(s[1])
print(s[2])

if s[0] == s[2]:
    print("Done")
else:
    print("Not Done")
"""

data = "This is a Good Day"
l = len(data)
print(l)
print(data[l-1])

# Slicing
print(data[0:3])
print(data[3:])
print(data[-1])
print("Data: ",data[1:-5])

if data.__contains__("Good"):
    print("Data contains Good")

words = data.split(" ")
print(words)

data = "class CA:"
if data.startswith("class"):
    words = data.split(" ")
    name = words[1]
    l = len(name)
    print(name[0:l-1])

songName = "hello.mp3"
if songName.endswith(".mp3"):
    print("This is a Valid Song")
else:
    print("This is an Invalid Song")

statement = "s1 = Student(101, 'John')"
if statement.__contains__("Student("):
    print("This is an Object Construction Statement")

# Assignment: Generate Permutation
# KnapSack Problem