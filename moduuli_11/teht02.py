class Auto():
    def __init__(self, registration_number, top_speed):
        self.registration_number = registration_number
        self.top_speed = top_speed
        self.current_speed = 0
        self.travel_distance = 0

    def accelerate(self, speed):
        new_speed = self.current_speed + speed
        if new_speed <= 0:
            self.current_speed = 0
        elif new_speed >= self.top_speed:
            self.current_speed = self.top_speed
        else:
            self.current_speed += speed

    def drive(self, time):
        self.travel_distance += self.current_speed * time

    def __str__(self):
        return f"NM: {self.registration_number}, CS: {self.current_speed} TS: {self.top_speed}, DIST: {self.travel_distance}"



"""Kirjoita aiemmin laatimallesi Auto-luokalle aliluokat Sähköauto ja Polttomoottoriauto. Sähköautolla on ominaisuutena akkukapasiteetti kilowattitunteina. Polttomoottoriauton ominaisuutena on bensatankin koko litroina. Kirjoita aliluokille alustajat. Esimerkiksi sähköauton alustaja saa parametreinaan rekisteritunnuksen, huippunopeuden ja akkukapasiteetin. Se kutsuu yliluokan alustajaa kahden ensin mainitun asettamiseksi sekä asettaa oman kapasiteettinsa. Kirjoita pääohjelma, jossa luot yhden sähköauton (ABC-15, 180 km/h, 52.5 kWh) ja yhden polttomoottoriauton (ACD-123, 165 km/h, 32.3 l). Aseta kummallekin autolle haluamasi nopeus, käske autoja ajamaan kolmen tunnin verran ja tulosta autojen matkamittarilukemat."""

class SahkoAuto(Auto):
    def __init__(self, registration_number, top_speed, battery):
        self.battery = battery
        
        super().__init__(registration_number, top_speed)

class PolttoMoottoriAuto(Auto):
    def __init__(self, registration_number, top_speed, gas):
        self.gas = gas 
        super().__init__(registration_number, top_speed)