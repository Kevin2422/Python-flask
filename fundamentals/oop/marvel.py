class Avenger:
    def __init__(self, name, speed, str, spandex, hp, flaw, true_iden):
        self.name = name
        self.speed = speed
        self.strength = str
        self.spandex = spandex
        self.hp = hp
        self.flaw = flaw
        self.true_iden = true_iden

    def intro(self):
        print(f"Hello my name is {self.name}")
        return self
    
    def party(self, *guest): #use asterisks when you don't know how many arguments are going to be passed through
        for x in guest:
            print(x.name)

    def party_of_3(self, guest1 = None, guest2 = None):
        if not guest1 and not guest2:
            print('looks like this is a one person party')
        print(f"{guest1}, {guest2}")


instance1 = Avenger("Captain America", 25, 98, "tight", 100, "water", "steve rogers")
print(instance1.hp)



