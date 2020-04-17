class IWalk:
    def __init__(self):
        self.movement = "walk"
        self.walk_speed = 1
    
    def move(self):
        print(f"Looks like we {self.movement}")
