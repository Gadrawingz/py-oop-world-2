# This one is for Sunday course on 24, 12, 2023
# From FreeCodeCamp in Legacy Python for everybody course
class PartyAnimal :
    # Some attributes
    x = 0
    name = ""
    
    def __init__(self, nm) :
        self.name = nm
        print(self.name, "Constructed!")
        
    def party(self) :
        self.x += 1 #  same as self.x = self.x + 1
        print(self.name, "party count: ", self.x)
    
    
