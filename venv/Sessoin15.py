# IS-A Relationship

# e-Commerce App
# We have so many Products | Mobile, TV, Shoe, Laptop etc...
"""
class Mobile:

    def __init__(self, pid, name, price, brand,  os, ram):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.os = os
        self.ram = ram

    def showMobileDetails(self):
        print("===",self.pid,self.name,"===")
        print("Price:",self.price)
        print("Brand:", self.brand)
        print("OS:", self.os)
        print("RAM:", self.ram)
        print("====================")

class TV:

    def __init__(self, pid, name, price, brand, screenSize, technology):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.screenSize = screenSize
        self.technology = technology

    def showTVDetails(self):
        print("===",self.pid,self.name,"===")
        print("Price:",self.price)
        print("Brand:", self.brand)
        print("Size:", self.screenSize)
        print("Technology:", self.technology)
        print("====================")

class Shoe:

    def __init__(self, pid, name, price, brand, size, color):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand
        self.size = size
        self.color = color

    def showShoeDetails(self):
        print("===",self.pid,self.name,"===")
        print("Price:",self.price)
        print("Brand:", self.brand)
        print("Size:", self.size)
        print("Color:", self.color)
        print("====================")
"""

class Product:

    def __init__(self, pid, name, price, brand):
        self.pid = pid
        self.name = name
        self.price = price
        self.brand = brand

    def showProductDetails(self):
        print("===", self.pid, self.name, "===")
        print("Price:", self.price)
        print("Brand:", self.brand)


# Inheritance Relationship | IS-A
class Mobile(Product):

    def __init__(self, pid, name, price, brand,  os, ram):
        Product.__init__(self, pid, name, price, brand)
        self.os = os
        self.ram = ram

    def showMobileDetails(self):
        Product.showProductDetails(self)
        print("OS:", self.os)
        print("RAM:", self.ram)
        print("====================")

class TV(Product):

    def __init__(self, pid, name, price, brand, screenSize, technology):
        Product.__init__(self, pid, name, price, brand)
        self.screenSize = screenSize
        self.technology = technology

    def showTVDetails(self):
        Product.showProductDetails(self)
        print("Size:", self.screenSize)
        print("Technology:", self.technology)
        print("====================")

class Shoe(Product):

    def __init__(self, pid, name, price, brand, size, color):
        Product.__init__(self, pid, name, price, brand)
        self.size = size
        self.color = color

    def showShoeDetails(self):
        Product.showProductDetails(self)
        print("Size:", self.size)
        print("Color:", self.color)
        print("====================")



m1 = Mobile(101, "iPhoneX", 80000, "Apple", "iOS", 4)
t1 = TV(201, "Samsung LED TV", 50000, "Samsung", 50, "OLED")
s1 = Shoe(301, "Alphabounce", 8000, "Adidas", 8, "Black")

m1.showMobileDetails()
t1.showTVDetails()
s1.showShoeDetails()