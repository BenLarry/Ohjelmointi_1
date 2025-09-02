import random

def dice_throw(face=6):
    return random.randint(1,face)

def main():
    dice = 0
    while dice != largest_face:
        dice = dice_throw(largest_face)
        print(dice)

largest_face = int(input("Kuinka suuren nopan haluat heittää: "))

main()