from movements import ISlither
from movements import ISwim
class Rattlesnake(ISlither, ISwim):

    def __init__(self, name, color):
        ISlither.__init__(self)
        ISwim.__init__(self)
        self.name = name
        self.color = color
   
    def __str__(self):
        return f'{self.name} the Rattlesnake'