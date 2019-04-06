# SVC
a = 10
print(a)

# MVC

# TUPLE - MVC which is IMMUTABLE
# b = 10, 20, 30, 40, 50
b = (10, 20, 30, 40, 50) # Homogeneous
print(b)
print(type(b))
print(b[3])
# This is not allowed. Tuple is just Read Only. IMMUTABLE
# b[2] = 111 # We are trying to change/update the data in Tuple

# This is not allowed. Tuple is just Read Only. IMMUTABLE
# b.append(60)
# c = 10, 'A', "John", 2.2 # Hetrogeneous
c = (10, 'A', "John", 2.2)
print(c)
print(c[1])

print()

# LIST - MVC which is MUTABLE | Supports Duplicacy (Redundancy)
d = [10, 20, 30, 40, 50, 20] # Homo
print(d)
print(type(d))
d[1] = 111
print(d)
d.append(60)
d.remove(40)
print(d)

e = [10, 'A', "John", 2.2] # Hetro

# SET - MVC which is MUTABLE | Does Not Supports Duplicacy (Redundancy)
f = {10, 20, 30, 40, 50, 20} # Homo
print(f) # Output is Un-Ordered due to Hashing (Explore)
g = {10, 'A', "John", 2.2}   # Hetro
print(type(f))

# Dictionary - MVC which is MUTABLE
# Dictionary | Word Meaning -> Key Value
words = {"discombobulated":"confused", "sharp":"which can hurt", "name":"identifier to a person"}
ages = {"john":20, "jennie":30, "jim":40}
employee = {"eid":101, 12:"Seating Floor", "salary":234567.124}

print(words)
print(ages)
print(employee)
print(type(words))
print(type(ages))

print(words["name"])
words["name"] = "identifier to anyone"
print(words)
