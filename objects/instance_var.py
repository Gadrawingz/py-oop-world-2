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
gd.add_trick('Cross Over')
mr.add_trick('3-point shooting!')
dn.add_trick('Playing Dead')

# Print data
print(gd.tricks)
print(mr.tricks)
print(dn.tricks)
