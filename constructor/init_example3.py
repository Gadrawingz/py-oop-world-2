class Dog:
    def __init__(self, dog_breed, dog_skin_color, dog_leg_nums):
        self.dog_breed = dog_breed
        self.dog_skin_color = dog_skin_color
        self.dog_leg_nums = dog_leg_nums

dog1 = Dog("Kush", "Brown", 4)
print(f'{dog1.dog_breed} is {dog1.dog_skin_color} and has {dog1.dog_leg_nums} legs!')
