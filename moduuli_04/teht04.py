import random

random_number = random.randint(1, 10)

while True:
    guess = int(input("Arvaa numero 1-10: "))

    if guess == random_number:
        print("Oikein")
        break
    elif guess > random_number:
        print("Liian suuri arvaus")
    else:
        print("liian pieni arvaus")