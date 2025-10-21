class Auto():
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.travel_distance = 0

def main():
    car = Auto("ABC-123", 142)
    print(f"rekisterutunnus: {car.registration_number}, Huippunopeus: {car.top_speed} km/h, Nopeus: {car.current_speed} km/h, ajettumatka: {car.travel_distance} km")
    
main()