"""

OOPS
====

Object Oriented Programming Structure

Design Methodolgy


Object
	Anything which we can see and touch
	Realtiy
	real time Entity

Class
	Representation of an Object
	Drawing of an Object

1. Think of an Object
2. Create its drawing
3. Looking from the drawing create it in real


Computer Science
Object is a multi value container
	it can store lot of data | Same Type (Homo), Diff Type (Hetro)

Food Delivery App
User should register in app. User should add his address.
User shall select a restaurant and select dishes from restaurant and finally place an order.
User shall make payments online or COD.

User : name, phone, email, gender, age
Address : adrsLine, city, state, zipCode, landmark
Restaurant : name, phone, email, address....
Dish : name, description, price, type, category
Order : oid, date, time, price

Class : Textual Representation of an Object

1. Think of an Object
2. Create its drawing / class
3. Looking from the drawing create it in real i.e. create an object

"""


# 1. Think of an Object: User : name, phone, email, gender, age

# 2. Create its Textual Representation i.e. class
class User:
    pass

# 3. From Class Create Real Objects
u1 = User() # Object Construction Statement
u2 = User() # Object Construction Statement

u3 = u1     # Reference Copy

print("u1 is:",u1)
print("u2 is:",u2)
print("u3 is:",u3)

# u1 and u2 are not objects, they are reference variables
# reference variables shall hold hashcode of Objects

# Create and write data in object
u1.name = "John"
u1.phone = "+91 99999 88888"
u1.email = "john@example.com"
u3.age = 20
u1.gender = "M"

u2.name = "Fionna"
u2.phone = "+91 77777 88888"
u2.email = "fionna@example.com"
u2.age = 23
u2.gender = "F"
u2.income = 50000
u2.weight = 55

# update data in object
u2.name = "Fionna Flynn"
u1.age = 33

# View data in Object
print(u1.__dict__)
print(u2.__dict__)
print(u3.__dict__)

# Delete Data From Object
del u1.gender
del u2.email

print(u1.__dict__)
print(u2.__dict__)