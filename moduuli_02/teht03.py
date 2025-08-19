base = input("Kirjota suorakulman kanta senttimetreinä: ")
height = input("Kirjota suorakulman korkeus senttimetreinä: ")

border = 2 * (int(base) + int(height))
area = int(base) * int(height)

print(f"Suorakulman piiri on {border} ja pinta-ala on {area} cm²")