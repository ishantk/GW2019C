class Parent:

    def purchaseBike(self):
        print(">> Lets Buy Bajaj Pulsar")

class Child(Parent):

    #Overriding
    # def purchaseBike(self):
    #     print(">> Lets Buy Royal Enfield")

    def purchaseBike(self, price):
        print(">> Lets Buy Royal Enfield")

    def purchaseBike(self, name="NA", price=50000):
        print(">> Lets Buy ",name, price)

cRef = Child()
cRef.purchaseBike(price=100000)
cRef.purchaseBike("Royal Enfield", 100000)

#Explore Firebase Firestore Database https://firebase.google.com/docs/firestore/quickstart?authuser=0