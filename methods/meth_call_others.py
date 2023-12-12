# Here I am creating a method that call other methods
# Here I have a class called a Bag
class Bag:
    def __init__(self):
        # This will contain data
        self.data = []
        
    # This method will add stuff(x) to a Bag
    def add_data(self, stuff):
        self.data = stuff
    
    # A method that calls another methods
    def add_data_twice(self, stuff):
        self.add_data(stuff)
        self.add_data(stuff)
    