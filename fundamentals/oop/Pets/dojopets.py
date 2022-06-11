
class Pet:
    def __init__(self, name, type, tricks, health, energy, sound):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy
        self.sound = sound
    def sleep(self):
        self.energy += 25
        print("energy ", self.energy)
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"energy {self.energy} and health {self.health}")
        return self

    def play(self):
        self.health += 5
        print("health", self.health)
        return self
    def noise(self):
        print(self.sound)
        return self


class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet
    def walk(self):
        self.pet.play()
        return self
    def feed(self):
        self.pet.eat()
        return self
    def bathe(self):
        self.pet.noise()
        return self

    
Rafdog = Pet("Bob", "dog", "fetch", 50, 50, "woof")
Raphael = Ninja("Raphael", "Mutant turtle", "pizza", "pizza", Rafdog)
Raphael.walk().feed().bathe()






