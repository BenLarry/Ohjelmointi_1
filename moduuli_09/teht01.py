from classes.auto import Auto

def main():
    car = Auto("ABC-123", 142)
    print(f"rekisterutunnus: {car.registration_number}, Huippunopeus: {car.top_speed} km/h, Nopeus: {car.current_speed} km/h, ajettumatka: {car.travel_distance} km")
    
main()