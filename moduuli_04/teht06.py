import random

amount = int(input("Kirjoita piste määrä: "))

in_circle = 0
tries = 0
while tries < amount:
    if random.uniform(-1, 1)**2 + random.uniform(-1,1)**2 < 1:
        in_circle += 1
    tries += 1

print(f"likiarvo: {4 * amount / amount}")