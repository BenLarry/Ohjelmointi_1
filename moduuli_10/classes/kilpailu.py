import random
from prettytable import PrettyTable
from classes.auto import Auto

class Kilpailu():
    def __init__(self, name, length, cars):
        self.name = name
        self.length = length
        self.cars = cars
        self.table = PrettyTable()
        self.table.field_names = ["Rekisteritunnus", "nopeus", "huippunopeus", "matka"]

    def tunti_kuluu(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def tulosta_tilanne(self):
        for car in self.cars:
            self.table.add_row([car.registration_number, car.current_speed, car.top_speed, car.travel_distance])
        return self.table

    def kilpailu_ohi(self):
        for car in self.cars:
            if car.travel_distance >= 10000:
                return True
        return False