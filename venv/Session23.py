def hello():
    print("Hello")

def bye():
    print("Bye")

class Student:
    def __init__(self, roll, name, phone):
        self.roll = roll
        self.name = name
        self.phone = phone

    def showStudent(self):
        print(self.roll,self.name,self.phone)

age = 30

# print("Wow!!")
# bye()