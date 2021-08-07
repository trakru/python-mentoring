
class Animal():
    """A simple class definition for all animals"""
    
    def __init__(self, name, age, species, pet):
        """Initialize name, age & species attributes"""
        self.name = name
        self.age = age
        self.species = species
        self.pet = pet
        
    def is_pettable(self, pet):
        """find if an animal can be a pet"""
        if self.pet == True:
            print(self.species.title() + "can be a pet")
        else:
            print(self.species.title() + "is unlikely to be a human pet")
