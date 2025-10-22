from classes.julkaisu import Julkaisu

class Lehti(Julkaisu):
    def __init__(self, nimi, paatoimittaja):
        self.paatoimittaja = paatoimittaja
        super().__init__(nimi)

    def tulosta_tiedot(self):
        print(f"Nimi: {self.nimi}, Päätoimittaja: {self.paatoimittaja}")