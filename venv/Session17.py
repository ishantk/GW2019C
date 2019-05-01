class CA:
    # Property of Class
    x = 10

    def __init__(self, a):
        CA.x = CA.x + a
        self.age = a

class CB(CA):
    def show(self):
        print("Age is:",self.age)
        print("x is: ",CB.x)

cRef = CB(20)
cRef.show()

# print(CA.__dict__)
# print(CB.__dict__)