class Employee:
    # Constructor:
    def __init__(self, name, salary, project):
        # data members
        self.name = name
        self.salary = salary
        self.project = project

    # Method to display employee's details
    def show_details(self):
        # accessing public data member
        print(f'Employee name is {self.name}, salary is {self.salary}')

    # method
    def task(self):
        print(self.name, 'is working on', self.project)
        
        
# Creating object of employee class ...
employee1 = Employee('Gad', '35000', 'Gadrawingz')

# Calling public method of the class
employee1.show_details()
employee1.task()
