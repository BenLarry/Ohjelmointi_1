from classes.kirja import Kirja
from classes.lehti import Lehti

def main():
    k = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
    k.tulosta_tiedot()

    l = Lehti("Aku Ankka", "Aki Hyyppä")
    l.tulosta_tiedot()

main()