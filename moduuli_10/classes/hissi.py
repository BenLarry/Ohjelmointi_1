class Hissi():
    def __init__(self, lowest_floor, highest_floor):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.floor = self.lowest_floor

    def move_to_floor(self, floor):
        while(self.floor > floor):
            print(self.move_down())

        while(self.floor < floor):
            print(self.move_up())

    def move_down(self):
        self.floor -= 1
        return f"Floor: {self.floor}"

    def move_up(self):
        self.floor += 1
        return f"Floor: {self.floor}"