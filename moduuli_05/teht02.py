
number = input("Kirjoita luku, tyhjä merkki lopettaa ohjelman: ")

list_of_numbers = []

while number != "":
    list_of_numbers.append(int(number))
    number = input("Kirjoita luku: ")

list_of_numbers.sort(reverse=True)

print(f"suurimmat luvut ovat: {list_of_numbers[0:5]}")