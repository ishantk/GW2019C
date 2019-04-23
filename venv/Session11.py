# OOPS : Object Oriented Programming Structure
# Object: Multi Value Container
# Class : Textual Representation for an Object

"""
    1. Think of an Object
    2. Draw an Object on paper
    3. From Drawing you create a real object

    example:
    1. Think of a Car
    2. Draw Car Design on Some Paper
    3. From Drawing create a real Car

    computer science:
    We will create a food delivery app. Requirements are listed below:
    1. user should register
    2. user should select a restaurant
    3. user should select dishes and add to cart
    4. user shall place the order and make payments

    > Extract data linked with some title

    User will have lot of data associated with it
    name
    email
    phone
    age
    gender
    address

    Restaurant
    name
    timings
    address
    .
    .....

    Dish
    image
    name
    description
    price
    type

    Order
    oid
    deliveryAddress
    price
    date
    time
    user
    restaurant

    Payment
    .
    ..
    ...


    Object > MVC which will have lot of data associated with it
    Class  > Textual Representation of an Object

     1. Think of an Object > User
     2. Create Textual Representation > Class
     3. Create an Object from Class

"""
# Textual Representation of an Object
class User:
    pass


# Object Construction Statement
u1 = User()
u2 = User()

# u1 and u2 can be any name of your choice
# u1 and u2 are called Reference Variables
# u1 and u2 shall hold HashCode of Object

print("u1 is:",u1)
print("u2 is:",u2)

# Write the data in Object
u1.name = "John"
u1.phone = "+91 99999 88888"
u1.age = 20

u2.name = "Fionna"
u2.phone = "+91 77777 88888"
u2.age = 22
u2.address = "Redwood Shores"
u2.email = "fionna@example.com"

# Delete data from Object
del u1.age
del u2.phone

# Update Operation
u1.name = "John Watson"
u1.salary = 30000 # Re Add another attribute

# Read Data from Object
print(u1.__dict__)
print(u2.__dict__)


