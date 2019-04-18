# 1. Create a single value storage container
a = 10
print("a in main has hashCode",hex(id(a)))

# 2. Create a function(method,procedure,routine) show
def show():
    a = 20
    b = 30
    print("a in show is:", a, "and hashcode is:",hex(id((a))))
    print("b in show is:", b, "and hashcode is:",hex(id((b))))

print("HashCode of show is: ",hex(id(show)))

# 3. Execute show function
show()

print("a is:", a)
# print("b is:", b) # This is error