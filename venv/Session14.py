class Order:

    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def showOrder(self):
        print("==",self.name,"==")
        print("Price:\u20b9",self.price)
        print("Quantity:",self.quantity)
        print("==================")

    def calculatePrice(self):
        return self.price * self.quantity




def showDicsountedPrice(total, promoCode):

    discountedPrice = 0

    print("Your Final Price is: \u20b9",discountedPrice)


o1 = Order("Paneer Tikka", 200, 2)
# o1.showOrder()

o2 = Order("Dry Manchurian", 100, 3)
# o2.showOrder()
        # 0    1
orders = [o1, o2]
# orders.append(o1) // 0
# orders.append(o2) // 1

# Add price of all the orders in total
total = 0

for i in range(0, len(orders)):
    orders[i].showOrder()
    print(orders[i].calculatePrice())

# FLAT50 -> 50% off in total value of orders is greater than 500 upto 250
# HI5    -> 25% off on all the total prices not greater than 1000

showDicsountedPrice(total , "FLAT50")