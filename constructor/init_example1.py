# Gad Iradufasha
class Student:

    # __init__ method(constructor)
    # Used to assign values to object properties
    # The properties are: name, marks
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

# init is called whenever a new class object is instantiated
student1 = Student("Paula", 40)
print(student1.name)
print(student1.marks)

student2 = Student("Patricia", 50)
print(student2.name)
print(student2.marks)