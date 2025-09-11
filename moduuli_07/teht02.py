names = set()

name = input("Kirjoita nimi(tyhjä merkkijono lopettaa objelman): ")
while name != "":
    if name not in names:
        print("Uusi nimi syötetty")
        names.add(name)
    else:
        print("Nimi syötetty aijemmin")
    
    name = input("Kirjoita nimi(tyhjä merkkijono lopettaa objelman): ")

print(f"Kaikki nimet syötetyt nimet: {names}")



##BUGINEN
