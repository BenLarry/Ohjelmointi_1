tuuma = 0
while tuuma >= 0:
    tuuma = int(input("Kirjoita koko tuumana: "))

    if tuuma < 0:
        break
    
    koko = tuuma * 2.54
    print(f"Koko {koko} cm")