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
        
    # A method that calls another methods(2)
    def add_data_triple(self, stuff):
        self.add_data(stuff)
        self.add_data(stuff)
        self.add_data(stuff)
    
# Calling 'em
bag1 = Bag()
bag1.add_data('Money')
bag1.add_data('Clothes')
print(bag1.data)