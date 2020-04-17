
from movements import IDig
from movements import IWalk

class Ant(IDig, IWalk):

    def __init__(self, name, color):
        IDig.__init__(self)
        IWalk.__init__(self)
        self.name = name
        self.color = color
   
    def __str__(self):
        return f'{self.name} the Ant'
