from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")

jack_sparrow = Pirate("Jack Sparrow")

michelangelo.attack(jack_sparrow).attack(jack_sparrow).meditate().attack(jack_sparrow).attack(jack_sparrow).attack(jack_sparrow).attack(jack_sparrow)
jack_sparrow.show_stats()