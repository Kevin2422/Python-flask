from random import randint, random


class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 10
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        if pirate.health > 0:
            if self.speed > pirate.speed and randint(1,2)>1:

                print(f"Ninja {self.name} throws two shuriken at {pirate.name}! Deals {self.strength*2} damage.")
                pirate.health -= self.strength*2
            else:
                print(f"Ninja {self.name} throws shuriken at {pirate.name}! Deals {self.strength} damage.")
                pirate.health -= self.strength
            if pirate.health <= 0:
                print(f"Ninja {self.name} has killed {pirate.name}!")
        elif pirate.health <= 0:
            print("Stop he's already dead")
        
        return self
            
    def meditate(self):
        print(f"Ninja {self.name} ponders the meaning of life")
        self.strength += 5
        self.speed +=1
        

        return self