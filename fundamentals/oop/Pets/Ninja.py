from dpet import Pet



class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    def walk(self):
        print(self.first_name , "'s pet" )
        self.pet.play()
        return self
    def feed(self):
        print(self.first_name, "'s pet")
        self.pet.eat()
        return self
    def bathe(self):
        print(self.pet.name, ":")
        self.pet.noise()
        return self


Rafdog = Pet("Bob", "dog", "fetch", 50, 50, "woof")
Rafdog.play()

Raphael = Ninja("Raphael", "Mutant turtle", "pizza", "pizza", Rafdog)
Raphael.walk().feed().bathe()