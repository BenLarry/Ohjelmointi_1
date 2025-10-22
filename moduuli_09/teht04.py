import random
from classes.auto import Auto

def main():
    cars = []
    for i in range(10):
        top_speed = random.randint(100, 200)
        cars.append(Auto(f"ABC-{i+1}", top_speed))

    while(True):
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
        
        for car in cars:
            if car.travel_distance >= 10000:
                print("winner: ", car)
                return

main()