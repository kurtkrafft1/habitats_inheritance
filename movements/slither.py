class ISlither:
    def __init__(self):
        self.movement = "slither"
        self.slither_speed = 1
    
    def move(self):
        print(f"Looks like we {self.movement}")
