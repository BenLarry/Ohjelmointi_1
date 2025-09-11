import mysql.connector


connect = mysql.connector.connect(
    host="127.0.0.1",
    database="flight_game",
    user="root",
    password="MetropoliaPass"
)

def search_coutry_airports(iso_country):
    sql = "SELECT type FROM airport WHERE iso_country = %s;"
    cursor = connect.cursor(dictionary=True)
    cursor.execute(sql, (iso_country,))
    result = cursor.fetchall()
    return result


def main():
    airport_types = {}
    iso_code = input("Kirjoita maan iso-koodi esim. (FI): ")
    airports = search_coutry_airports(iso_code)
    if airports is None:
        print(f"maassa iso koodilla {iso_code} ei ole lentoasemia")
        return
    
    for airport in airports:
        airport_type = airport['type']
        if airport_type in airport_types:
            airport_types[airport_type] += 1
        else:
            airport_types[airport_type] = 1
        
    for type in airport_types:
        print(f"Lentoasema tyyppi: {type} on {airport_types[type]} kappaletta")
main()