leviskat = float(input("anna leviskät: "))
naulat = float(input("anna naulat: "))
luodit = float(input("anna luodit: "))

luodin_paino = 13.3
naulan_paino = 32 * luodin_paino
leviska_paino = 20 * naulan_paino

paino_grammoissa = (leviskat * leviska_paino) + (naulat * naulan_paino) + (luodit * luodin_paino)
grammat = paino_grammoissa % 1000
kilogrammat = int(paino_grammoissa / 1000)
print("Massa nykymittojen mukaan: ")
print(f"{kilogrammat} kilogrammaa ja {grammat:.2f} grammaa.")
