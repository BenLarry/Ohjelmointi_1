"""Nyt ohjelmoidaan autokilpailu. Uuden auton kuljettu matka alustetaan automaattisesti nollaksi. Tee pääohjelman alussa lista, joka koostuu kymmenestä toistorakenteella luodusta auto-oliosta. Jokaisen auton huippunopeus arvotaan 100 km/h ja 200 km/h väliltä. Rekisteritunnus luodaan seuraavasti "ABC-1", "ABC-2" jne. Sitten kilpailu alkaa. Kilpailun aikana tehdään tunnin välein seuraavat toimenpiteet:

Jokaisen auton nopeutta muutetaan siten, että nopeuden muutos arvotaan väliltä -10 ja +15 km/h väliltä. Tämä tehdään kutsumalla kiihdytä-metodia.
Kaikkia autoja käsketään liikkumaan yhden tunnin ajan. Tämä tehdään kutsumalla kulje-metodia.
Kilpailu jatkuu, kunnes jokin autoista on edennyt vähintään 10000 kilometriä. Lopuksi tulostetaan kunkin auton kaikki ominaisuudet selkeäksi taulukoksi muotoiltuna."""
import random

class Auto():
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.travel_distance = 0

    def accelerate(self, speed):
        self.current_speed += speed

    def travel(self, time):
        self.travel_distance = self.current_speed * time

def main():
    cars = []
    for i in range(0, 10):
        top_speed = random.randint(100, 200)
        cars.append(Auto(f"ABC-{i+1}", top_speed))

    race = True
    while(race):
        for car in cars:
            car.accelerate(random.randint(-10, 15))
            car.travel(1)

            if car.travel_distance >= 10000:
                race = False
                print("Winner", car.registration_number, car.travel_distance)
                break


            print(car.registration_number, car.travel_distance)


main()