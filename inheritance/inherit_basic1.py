# My Base class
class Animal:
    task = ["One", "Two"]
    def eat(self):
        global task        
        print(f'Task {task[0]}')
        
    def walk(self):
        global task        
        print(f'Task {task[0]}')
    