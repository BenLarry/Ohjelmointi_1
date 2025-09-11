import mysql.connector
from geopy import distance


connect = mysql.connector.connect(
    host="127.0.0.1",
    database="flight_game",
    user="root",
    password="MetropoliaPass"
)

def search_airport(ICAO_code):
    sql = "SELECT latitude_deg, longitude_deg FROM airport WHERE ident = %s"
    cursor = connect.cursor()
    cursor.execute(sql, (ICAO_code,))
    result = cursor.fetchone()
    return result

def distance_between_airports(airport_one, airport_two):
    return distance.distance(airport_one, airport_two)

def main():
    ICAO_one = input("Anna lentoaseman ICAO koodi: ")
    ICAO_two = input("Anna toisen lentokoneen ICAO koodi: ")

    airport_one = search_airport(ICAO_one)
    airport_two = search_airport(ICAO_two)

    result = distance_between_airports(airport_one, airport_two)
    print(f"lentoasemien välinen matka on {result.kilometers:.0f} km")


main()
