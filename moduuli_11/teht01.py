"""Toteuta seuraava luokkahierarkia Python-kielellä: Julkaisu voi olla kirja tai lehti. Jokaisella julkaisulla on nimi. Kirjalla on lisäksi kirjoittaja ja sivumäärä, kun taas lehdellä on päätoimittaja. Kirjoita luokkiin myös tarvittavat alustajat. Tee aliluokkiin metodi tulosta_tiedot, joka tulostaa kyseisen julkaisun kaikki tiedot. Luo pääohjelmassa julkaisut Aku Ankka (päätoimittaja Aki Hyyppä) ja Hytti n:o 6 (kirjailija Rosa Liksom, 200 sivua). Tulosta molempien julkaisujen kaikki tiedot toteuttamiesi metodien avulla"""

from classes.kirja import Kirja
from classes.lehti import Lehti

def main():
    k = Kirja("Hytti n:o 6", "Rosa Liksom", 200)
    k.tulosta_tiedot()

    l = Lehti("Aku Ankka", "Aki Hyyppä")
    l.tulosta_tiedot()

main()