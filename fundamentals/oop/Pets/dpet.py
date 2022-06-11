
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
        print(self.name, "'s")
        print("energy ", self.energy)
        return self
    def eat(self):
        self.energy += 5
        self.health += 10
        print(self.name, "'s")
        print(f"energy {self.energy} and health {self.health}")
        return self

    def play(self):
        self.health += 5
        print(self.name, "'s")
        print("health", self.health)
        return self
    def noise(self):
        print(self.sound)
        return self

class Cat(Pet):
    def __init__(self, name, type, tricks, health, energy, sound, fur):
        super().__init__(name, type, tricks, health, energy, sound,)
        self.fur = fur
    def sleep(self):
        print("cat is purring")
        super().sleep()

henry = Cat('henry', 'd', 'd', 55, 55,'d','f')
henry.sleep()

