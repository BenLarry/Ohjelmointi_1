from classes.auto import Auto

def main():
    car = Auto("ABC-123", 150)
    print(f"rekisterutunnus: {car.registration_number}, Huippunopeus: {car.top_speed} km/h, Nopeus: {car.current_speed} km/h, ajettumatka: {car.travel_distance} km")

    print("0", car.current_speed)
    car.accelerate(30)
    print("30", car.current_speed)
    car.accelerate(70)
    print("100", car.current_speed)
    car.accelerate(50)
    print("150", car.current_speed)
    car.accelerate(100)
    print("150", car.current_speed)
    car.accelerate(200)
    print("150 XD", car.current_speed)
    car.accelerate(-100)
    print("50", car.current_speed)

    car.drive(2)
    print(car.travel_distance)

main()