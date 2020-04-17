class IFly:
    def __init__(self):
        self.movement = "fly"
        self.fly_speed = 1
    
    def move(self):
        print(f"Looks like we {self.movement}")
