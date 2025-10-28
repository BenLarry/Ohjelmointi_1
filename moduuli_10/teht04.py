import random
from classes.kilpailu import Kilpailu
from classes.auto import Auto

def main():
    cars = []
    for i in range(10):
        top_speed = random.randint(100, 200)
        cars.append(Auto(f"ABC-{i+1}", top_speed))

    kilpailu = Kilpailu("Suuri romuralli", 8000, cars)

    race_over = kilpailu.kilpailu_ohi()
    while(not race_over):
        kilpailu.tunti_kuluu()
        race_over = kilpailu.kilpailu_ohi()
    
    print(kilpailu.tulosta_tilanne())
    
    

    


main()