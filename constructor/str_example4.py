# Lets construct a shit!
class Cylinder:
    pi = 3.14
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
    
    def __str__(self):
        return "Called __str__"

    def __repr__(self):
        return "Called __repr__"

cy1 = Cylinder(30, 70)
print(cy1)
print(repr(cy1))
print(str(cy1))

# For more edits to come!