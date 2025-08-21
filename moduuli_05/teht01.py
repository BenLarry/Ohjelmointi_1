
import random

dice_amount = int(input("Anna noppien lukumäärä: "))

total = 0
for dice in range(dice_amount):
    total += random.randint(1, 6)

print(f"noppien summa on {total}")