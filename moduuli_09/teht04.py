import random
from classes.auto import Auto

def main():
    cars = []
    for i in range(10):
        top_speed = random.randint(100, 200)
        cars.append(Auto(f"ABC-{i+1}", top_speed))

    distance = 0
    while(distance <= 10000):
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)
            if car.travel_distance >= 10000:
                distance = car.travel_distance
                print("winner: ", car)

main()