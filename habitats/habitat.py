class Habitat:

    def __init__(self):
        self.animals = set()
    
    def add_animal(self, animal):
        self.animals.add(animal)
        print(f"{animal} was added to the habitat!")