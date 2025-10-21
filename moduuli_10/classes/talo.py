from classes.hissi import Hissi

class Talo():
    def __init__(self, lowest_floor, highest_floor, elevator_amount):
        self.lowest_floor = lowest_floor
        self.highest_floor = highest_floor
        self.elevators = []
        for i in range(elevator_amount):
            self.elevators.append(Hissi(lowest_floor, highest_floor))

    def use_elevator(self, elevator_number, floor):
        elevator = self.elevators[elevator_number-1]
        elevator.move_to_floor(floor)

    def fire_alarm(self):
        for elevator in self.elevators:
            elevator.move_to_floor(self.lowest_floor)