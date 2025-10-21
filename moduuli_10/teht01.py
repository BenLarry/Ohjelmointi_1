from classes.hissi import Hissi

def main():
    h = Hissi(1, 10)
    h.move_to_floor(7)
    h.move_to_floor(3)
    print(h.floor)

main()