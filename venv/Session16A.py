class Point:

    count = 0

    def __init__(self):
        # print(">> init executed")
        Point.count = Point.count + 1

    def showCount(self):
        print("count is:",Point.count)

# p1 = Point() # 1
# p2 = Point() # 2
# p3 = Point()

for i in range(1,100): # 99 times
    p = Point()

# print(p1.__dict__)
# print(p2.__dict__)
# print(p3.__dict__)

# p1.showCount() # 3
# p2.showCount() # 3
# p3.showCount() # 3

p1 = Point()
p1.showCount()

