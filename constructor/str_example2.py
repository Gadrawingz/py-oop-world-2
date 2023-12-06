class Ghetto:
  def  __init__(self, rent_fees, rooms, location):
    self.rfs = rent_fees
    self.rno = rooms
    self.loc = location
  
  def  __str__(self):
    return  "My ghetto from {} with {} rooms is paid {} a month".format(self.loc, self.rno, self.rfs)

ghetto1 = Ghetto(25000, 2, "Huye")
print(ghetto1)
print(str(ghetto1))
print(ghetto1.__str__())
