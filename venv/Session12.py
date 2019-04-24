# OOPS
# Object : Multi Value Container
# Class  : Representation of an Object
# eCommerce Platform
# Customer Object
# Address Object
# Customer HAS-AN Address | HAS-A Relation
# HAS-A Relation | 1 to 1 or 1 to many

class Customer:
    # Constructor : Standardize what should be in the Object
    def __init__(self, name, phone, email, address):
        # LHS | self.fullName -> create an attribute called fullName in Object
        # RHS | name -> copy value of name into object's attribute
        self.fullName = name
        self.phone = phone
        self.email = email
        self.address = address
        # print("HashCode for self:", hex(id(self)))


class Address:
    def __init__(self, a, city, state, zipCode):
        self.adrsLine = a
        self.city = city
        self.state = state
        self.zipCode = zipCode


# Object Construction Statement

a1 = Address("Pristine Magnum", "Bengaluru", "Karnataka", 520001)
a2 = Address("Country Homes", "Ludhiana", "Punjab", 141002)

numbers = [10, 20] # List of Numbers
#            0    1
addresses = [a1, a2] # List of reference variables
# Now we shall copy hashcode of address list

c1 = Customer("John", "+91 99999 88888", "john@example.com", addresses)

for i in range(0, len(c1.address)):
    print(c1.address[i].__dict__)

print(c1.__dict__)

"""
name = input("Enter Your Name:")

c1 = Customer(name, "+91 99999 88888", "john@example.com", a1) # Customer() -> execute __init__ automatically
print("HashCode for c1:",hex(id(c1)))
print("HashCode for a1:",hex(id(a1)))

print(a1.__dict__)
print(c1.__dict__)
print(c1.address.__dict__)
"""