"""tehtävä on jatkoa aiemmalle autokilpailutehtävälle. Kirjoita Kilpailu-luokka, jolla on ominaisuuksina kilpailun nimi, pituus kilometreinä ja osallistuvien autojen lista. Luokassa on alustaja, joka saa parametreinaan nimen, kilometrimäärän ja autolistan ja asettaa ne ominaisuuksille arvoiksi. Luokassa on seuraavat metodit:

tunti_kuluu, joka toteuttaa aiemmassa autokilpailutehtävässä mainitut tunnin välein tehtävät toimenpiteet eli arpoo kunkin auton nopeuden muutoksen ja kutsuu kullekin autolle kulje-metodia.
tulosta_tilanne, joka tulostaa kaikkien autojen sen hetkiset tiedot selkeäksi taulukoksi muotoiltuna.
kilpailu_ohi, joka palauttaa True, jos jokin autoista on maalissa eli se on ajanut vähintään kilpailun kokonaiskilometrimäärän. Muussa tapauksessa palautetaan False.
Kirjoita pääohjelma, joka luo 8000 kilometrin kilpailun nimeltä "Suuri romuralli". Luotavalle kilpailulle annetaan kymmenen auton lista samaan tapaan kuin aiemmassa tehtävässä. Pääohjelma simuloi kilpailun etenemistä kutsumalla toistorakenteessa tunti_kuluu-metodia, jonka jälkeen aina tarkistetaan kilpailu_ohi-metodin avulla, onko kilpailu ohi. Ajantasainen tilanne tulostetaan tulosta tilanne-metodin avulla kymmenen tunnin välein sekä kertaalleen sen jälkeen, kun kilpailu on päättynyt."""
import random
from classes.auto import Auto
from prettytable import PrettyTable


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


def main():
    cars = []
    for i in range(10):
        top_speed = random.randint(100, 200)
        cars.append(Auto(f"ABC-{i+1}", top_speed))

    kilpailu = Kilpailu("Suuri romuralli", 8000, cars)

    race_over = kilpailu.kilpailu_ohi()
    while(not race_over):
        kilpailu.tunti_kuluu()
        race_over = kilpailu.kilpailu_ohi()
    
    print(kilpailu.tulosta_tilanne())
    
    

    


main()