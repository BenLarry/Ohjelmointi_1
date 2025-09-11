import mysql.connector


connect = mysql.connector.connect(
    host="127.0.0.1",
    database="flight_game",
    user="root",
    password="MetropoliaPass"
)

def search_coutry_airports(iso_country):
    sql = "SELECT type, count(*) AS count FROM airport WHERE iso_country = %s GROUP BY type"
    cursor = connect.cursor(dictionary=True)
    cursor.execute(sql, (iso_country,))
    result = cursor.fetchall()
    return result


def main():
    iso_code = input("Kirjoita maan iso-koodi esim. (FI): ")
    airports = search_coutry_airports(iso_code)
    for airport in airports:
        print(f"{airport['type']} on {airport['count']} kappaletta")
main()