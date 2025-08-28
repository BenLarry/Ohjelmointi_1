import random

def dice_throw():
    return random.randint(1,6)

def main():
    dice = 0
    while dice != 6:
        dice = dice_throw()
        print(dice)

main()
        
    