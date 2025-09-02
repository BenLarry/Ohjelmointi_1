def gallons_to_liters(gallons):
    return gallons * 3.785

def main():
    gallons = float(input("Anna bensiinimäärä galloina: "))
    while gallons > 0:
        print(gallons_to_liters(gallons))
        gallons = float(input("Anna bensiinimäärä galloina: "))

main()