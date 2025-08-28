alkuluku = False
number = int(input("anna kokonaisluku: "))

while number == 1:
    print("anna luku korkeampi kuin 1")
    number = int(input("anna kokonaisluku: "))

for num in range(2, number):
    if number % num == 0:
        alkuluku = False
        break
    else:
        alkuluku = True


print(alkuluku)

