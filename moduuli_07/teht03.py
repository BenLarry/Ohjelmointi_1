airports = {}

def hae_lentoasema(code):
    if code in airports:
        return airports[code]
    return "Lentoasemaa ei löytynyt!"

def talenna_lentoasema(code, name):
    airports[code] = name
    return airports[code]

def main():
    while True:
        user_input = input("Jos haluat hakea tietoa paina (1), jos halaut syöttää tietoa paina (2), Mikä muu nimimerkki lopettaa ohjelman!: ")

        if user_input != int or user_input == "":
            return

        if int(user_input) == 1:
            ICAO_code = input("anna ICAO koodi: ")
            print(hae_lentoasema(ICAO_code))        
        elif int(user_input) == 2:
            ICAO_code = input("anna ICAO koodi: ")
            name = input("Anna lentoaseman nimi: ")
            print(f" Lentoasema {talenna_lentoasema(ICAO_code, name)} on tallenettu")
        else:
            return

main()
