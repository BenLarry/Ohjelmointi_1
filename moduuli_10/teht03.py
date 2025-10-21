from classes.talo import Talo

def main():
    house = Talo(1, 10, 2)

    print(house.elevators[0].floor)
    house.use_elevator(1,5)
    print(house.elevators[0].floor)
    house.fire_alarm()
    print(house.elevators[0].floor)

main()


