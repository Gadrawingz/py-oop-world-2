"""
Encapsulation:
--------------
-It refers to the bundling of attributes and methods inside a single class.
-It prevents outer classes from accessing and changing attributes and
methods of a class. This also helps to achieve data hiding.

-In Python, we denote private attributes using underscore as the prefix
i.e. single _ or double __
"""


class Smartphone:

    # Some attributes
    def __init__(self):
        self.__minimum_price = 100000
        self.__maximum_price = 500000

    def sell_smartphone(self):
        print("Selling price : {}".format(self.__maximum_price))

    def set_maximum_price(self, price):
        self.__maximum_price = price


# Something down here!
phone1 = Smartphone()
phone1.sell_smartphone()

# I changed the current price!
phone1.__maximum_price = 435000
phone1.sell_smartphone()

# I changed the current price using setter func!
phone1.set_maximum_price(770500)
phone1.sell_smartphone()
