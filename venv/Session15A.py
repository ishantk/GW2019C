class Parent:

    def __init__(self, wealth, vehicle):
        self.wealth = wealth
        self.vehicle = vehicle

class Child(Parent):

    def __init__(self, companyName, salary):
        self.companyName = companyName
        self.salary = salary


# p1 = Parent(wealth=100000, vehicle=3)
# p1 = Parent(100000, 3)
# print(p1.__dict__)

# c1 = Child(100000, 3)
# print(c1.__dict__)

c1 = Child("ABC International", 30000)
print(c1.__dict__)

"""
    Zomato : Identify Inheritance Relationships and Code it !!

"""
