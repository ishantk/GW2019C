"""
class User:

    # Constructor
    def __init__(self):
        print(">> init executed")
        print("self is:",hex(id(self)))
        # self is a reference variable which contains hashcode of current object in action

u1 = User()
u2 = User()

print("u1 is:",hex(id(u1)))
print("u2 is:",hex(id(u2)))
"""

class User:
    # Object Standardization
    def __init__(self, name, phone, email):
        self.fullName = name
        self.phone = phone
        self.email = email


u1 = User("George", "+91 99999 88888", "george@example.com")
u2 = User("Sia", "+91 77777 88888", "sia@example.com")

u1.income = 33000
u1.weight = 55

print(u1.__dict__)
print(u2.__dict__)
