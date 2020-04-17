
from movements import IWalk
from movements import ISwim

class Terrapin(IWalk, ISwim):

    def __init__(self, name, color):
        ISwim.__init__(self)
        IWalk.__init__(self)
        self.name = name
        self.color = color
   
    def __str__(self):
        return f'{self.name} the Terrapin'
