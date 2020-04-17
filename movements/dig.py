class IDig:
    def __init__(self):
        self.movement = "dig"
        self.dig_speed = 1
    
    def move(self):
        print(f"Looks like we {self.movement}")
