# Standardizing the Object
class User:

    # Constructor
    # which is executed automatically when we create an Object
    def __init__(self, name, age, address):
        print(">> init executed")
        print(">> self is:",self)
        self.fullName = name
        self.age = age
        self.address = address

# Object Construction Statement
u1 = User("John", 22, "Redwood Shores")
u2 = User("Fionna", 26, "Pristine Magnum")
print(">> u1 is:",u1)

u1.salary = 40000
u2.phone = "+91 99999 88888"

u1.age = 33

del u1.fullName

print(u1.__dict__)
print(u2.__dict__)

