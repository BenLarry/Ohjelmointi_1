
number = input("Kirjoita luku, tyhjä merkki lopettaa ohjelman: ")

list_of_numbers = []

while number != " ":
    list_of_numbers.append(int(number))
    number = input("Kirjoita luku: ")

list_of_numbers.sort(reverse=True)

largest_nums = []
for i, num in enumerate(list_of_numbers):
    if i == 5:
        break
    largest_nums.append(num)

print(f"suurimmat luvut ovat: {largest_nums}")