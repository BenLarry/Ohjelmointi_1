def calc_pizza_prize_per_squarecm(pizza_diameter, prize):
    PI = 3.14
    radius = pizza_diameter / 2
    area = PI * radius * radius
    prize_per_squarecm = area / prize
    return prize_per_squarecm

def main():
    pizza_one_diameter = float(input("Kirjoita pizzan halkasija cm: "))
    pizza_one_prize = float(input("Kirjoita pizzan hinta: "))
    
    pizza_two_diameter = float(input("Kirjoita toisen pizzan halkasija cm: "))
    pizza_two_prize = float(input("Kirjoita toisen pizzan hinta: "))

    pizza_one_prize_per_squarecm = calc_pizza_prize_per_squarecm(pizza_one_diameter, pizza_one_prize)
    pizza_two_prize_per_squarecm = calc_pizza_prize_per_squarecm(pizza_two_diameter, pizza_two_prize)

    if pizza_one_prize < pizza_two_prize_per_squarecm:
        print("ensinmmäinen pizza edullisempi")
    elif pizza_one_prize_per_squarecm == pizza_two_prize_per_squarecm:
        print("pizzat saman hintasia")
    else:
        print("toinen pizza edullisempi")

main()