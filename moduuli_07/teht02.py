names = set()

name = None
while name != "":
    name = input("Kirjoita nimi(tyhjä merkkijono lopettaa objelman): ")
    if name not in names:
        print("new: ", name)
        names.add(name)
        last_name = name
    else:
        print("last: ", last_name)
    




