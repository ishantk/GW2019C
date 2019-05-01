class Point:

    def __init__(self, x, y, z):
        self.x = x
        self._y = y
        self.__z = z

    # _  is protected
    # __ is private -> Name Mangling | _ClassName__z

    def __showPoint(self):
        print("Point is:",self.x, self._y, self.__z)

p1 = Point(10, 20, 30)
# p1.showPoint() error
print(p1.x)
print(p1._y)
# print(p1.__z) error
print(p1._Point__z)

print(p1.__dict__)

p1._Point__showPoint()