
season = ("talvi", "kevät", "kesä", "syksy")
month  = int(input("Kirjoita kuukauden numero(1-12): "))

if month <= 0 or month > 12:
    print("syötö numero 1-12")
elif 2 >= month or month == 12:
    print(season[0])
elif 3 <= month < 6:
    print(season[1])
elif 6 <= month < 9:
    print(season[2])
else:
    print(season[3])


#BUGEINEN JA KESKEN