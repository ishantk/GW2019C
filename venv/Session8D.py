def update(a):
    print("a before is:",a,"and hashCode is",hex(id(a)))
    a = a * 2
    print("a after is:", a, "and hashCode is", hex(id(a)))

z = 10
print("z before is: ",z, "and hashCode is",hex(id(z)))
update(z) # execution |  Pass By Value
print("z after is: ",z, "and hashCode is",hex(id(z)))
