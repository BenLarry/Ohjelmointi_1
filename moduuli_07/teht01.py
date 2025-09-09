
season = ("talvi", "talvi", "kevät", "kevät", "kevät", "kesä", "kesä", "kesä", "syksy", "syksy", "syksy", "talvi")
month  = int(input("Kirjoita kuukauden numero(1-12): "))

if month >= 1 and month <= 12:
    print(f"kuukausi {month} on {season[month-1]}")
    
