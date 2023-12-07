# My Base class
class Animal:
    
    def eat(self):      
        print(f'Animal: Eating')
        
    def walk(self):     
        print(f'Animal: Walking')
    
# Creation of derived class
class Dog(Animal):
    def bark(self):
        print("Dog Act: Barking!")

# Create object of the Dog class
dog1 = Dog()
# Calling members of the base class
dog1.eat()
dog1.walk()

# Calling member of the derived class
dog1.bark()