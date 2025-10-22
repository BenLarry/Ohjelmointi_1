from classes.julkaisu import Julkaisu

class Kirja(Julkaisu):
    def __init__(self, nimi, kirjoittaja, sivumaara):
        self.kirjoittaja = kirjoittaja
        self.sivumaara = sivumaara
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}, Kirjoittaja: {self.kirjoittaja}, Sivumäärä: {self.sivumaara}")