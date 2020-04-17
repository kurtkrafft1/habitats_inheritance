from .habitat import Habitat


class Terrarium(Habitat):

    def __init__(self):
        super().__init__()

    def add_animal(self, animal):
        try:
            if animal.walk_speed > 0:

                self.animals.add(animal)
                print(f"Nice! {animal} was added to the {self}")

        except AttributeError:
            pass
        try:
            if animal.dig_speed > 0:

                self.animals.add(animal)
                print(f"Nice! {animal} was added to the {self}")

        except AttributeError:

            try:
                if animal.slither_speed > 0:

                    self.animals.add(animal)
                    print(f"Nice! {animal} was added to the {self}")

            except AttributeError:
                print(f"Sorry, {animal} is not allowed in the {self}.")

    def remove_animal(self, animal):
        try:
            animal.remove(animal)
            print(f"{animal} was removed from the {self}")
        except ValueError:
            print(f'I am sorry, {animal} was not in the {self}.')

    def __str__(self):
        return "Thales Terrarium"
