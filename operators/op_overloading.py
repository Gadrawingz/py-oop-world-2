# The (+) operator overloading
# We will need to implement __add__() function in the class.
# To overload the + operator.
class Point:

    def __int__(self, a=0, b=0):
        self.a = a
        self.b = b

    def __str__(self):
        return "({0},{1})".format(self.a, self.b)

    def __add__(self, other):
        a = self.a + other.a
        b = self.b + other.b
        return Point(a, b)

p1 = Point(1, 2)
p2 = Point(2, 3)
print(p1+p2)