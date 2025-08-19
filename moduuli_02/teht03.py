base = float(input("Kirjota suorakulman kanta senttimetreinä: "))
height = float(input("Kirjota suorakulman korkeus senttimetreinä: "))

border = 2 * (base + height)
area = base * height

print(f"Suorakulman piiri on {border} ja pinta-ala on {area} cm²")