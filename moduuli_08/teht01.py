import mysql.connector


connect = mysql.connector.connect(
    host="127.0.0.1",
    database="flight_game",
    user="root",
    password="MetropoliaPass"
)

def search_airport(code):
    sql = "SELECT name, municipality FROM airport WHERE ident = %s;"
    cursor = connect.cursor(dictionary=True)
    cursor.execute(sql, (code,))
    result = cursor.fetchone()
    return result

def main():
    ICAO_code = input("Kirjoita lentoaseman ICAO koodi: ")
    airport = search_airport(ICAO_code)
    if airport is None:
        print(f"Lentoasemaa ICAO-koodilla {ICAO_code} ei löytynyt")
        return
    
    print(f"Lentoasema {airport['name']} on kunalla {airport['municipality']}")


main()
