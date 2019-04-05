age = 10
print("age is:",age)
print("HashCode of age is:",id(age))

# This gives is back some number 28 (bytes/bits ?) | Explore
print("Size of age is:",age.__sizeof__())

print("HashCode of age in binary is:",bin(id(age)))
print("HashCode of age in hexadecimal is:",hex(id(age)))
print("HashCode of age in octal is:",oct(id(age)))

print("type of age is:",type(age))

pi = 3.14
print("type of pi is:",type(pi))

ages = 10, 20, 30, 40, 50
print("type of ages is:",type(ages))