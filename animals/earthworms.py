
from movements import IDig


class EarthWorm(IDig):

    def __init__(self, name, color):
        super().__init__()
        self.name = name
        self.color = color
   
    def __str__(self):
        return f'{self.name} the Earthworm'
