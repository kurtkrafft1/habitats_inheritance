
from movements import IFly

class Finch(IFly):

    def __init__(self, name, color):
        super().__init__()
        self.name = name
        self.color = color
   
    def __str__(self):
        return f'{self.name} the Finch'
