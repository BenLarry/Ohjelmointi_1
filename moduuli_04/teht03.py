numbers = []
while True:
    num = input("kirjoita luku: ")
    
    if num == " ":
        print(f"Pienin luku {min(numbers)} ja suurin luku {max(numbers)}")
        break

    numbers.append(int(num))