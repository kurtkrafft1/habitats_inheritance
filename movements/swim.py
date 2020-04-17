class ISwim:
    def __init__(self):
        self.movement = "swim"
        self.swim_speed = 1
    
    def move(self):
        print(f"Looks like we {self.movement}")
