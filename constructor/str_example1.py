class Student:
    def __init__(self, student_name, student_age):
        self.name = student_name
        self.age  = student_age
    
    def __str__(self):
        return f'The name is {self.name} and age is {self.age}'

    def __repr__(self):
        return f'Ocean(\'{self.name}\', {self.age})'

student1 = Student('Zetro', 19)
print(str(student1))
print(repr(student1))
