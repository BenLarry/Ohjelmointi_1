names = set()

name = None
while name != "":
    name = input("Kirjoita nimi(tyhjä merkkijono lopettaa objelman): ")
    if name not in names:
        print("Uusi nimi syötetty")
        names.add(name)
    else:
        print("Nimi syötetty aijemmin")
    




