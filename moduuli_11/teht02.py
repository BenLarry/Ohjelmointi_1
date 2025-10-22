from classes.polttoMoottoriAuto import PolttoMoottoriAuto
from classes.sahkoAuto import SahkoAuto

def main():
    e_car = SahkoAuto("ABC-1", 180, 52.5)
    gas_car = PolttoMoottoriAuto("ABC-2", 165, 32.3)

    e_car.accelerate(30)
    gas_car.accelerate(100)
    
    e_car.drive(3)
    gas_car.drive(3)

    print("Sähkö auto: ", e_car)
    print("Bensa auto: ", gas_car)

main()

