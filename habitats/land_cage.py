from .habitat import Habitat
class LandCage(Habitat):
    
    def __init__(self):
        super().__init__()
    
    def add_animal(self, animal):
        try:
            if animal.walk_speed >0 :
                self.animals.add(animal)
                print(f"{animal} was temporarily stored in the land cage")
        except AttributeError:
            pass

        try:
            if animal.dig_speed >0 :
                self.animals.add(animal)
                print(f"{animal} was temporarily stored in the land cage")
        except AttributeError:
            try:
                if animal.slither_speed >0 :
                    self.animals.add(animal)
                    print(f"{animal} was temporarily stored in the land cage")
            except AttributeError:
                print(f"I am sorry {animal} cant be added to the {self}")


    
    def remove_animal(self, animal):
        try:
            animal.remove(animal)
            print(f"{animal} was removed from the {self}")
        except ValueError:
            print(f'I am sorry, {animal} was not in this cage.')
        
    def __str__(self):
        return "Land Cage"