# Gad created class named Person
# But, Person created has tricks
class Person:
    
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender
        self.tricks = []
        
    def add_trick(self, trick):
        self.tricks.append(trick)

# Jumping out of class!
gd = Person('Gad', 'Male')
mr = Person('Maria', 'Female')
dn = Person('Danny', 'Danny')

# Adding...
a1 = gd.add_trick('Cross Over')
a2 = gd.add_trick('3-point shooting!')
a3 = mr.add_trick('Playing Dead')

# Print data
print(a1)
print(a2)
print(a3)
