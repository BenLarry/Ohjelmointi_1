gender = input("Anna sukupuolesi (M tai N): ")
hemoglobin_level = float(input("Anna hemoglobiiniarvo: "))

if gender.lower() == "m":
    if hemoglobin_level > 195:
        print("hemoglobiini tasot suuret")
    elif hemoglobin_level < 134:
        print("hemoglobiini tasot alhaset")
    else:
        print("hemoglobiini tasot normaali")

elif gender.lower() == "n":
    if hemoglobin_level > 175:
        print("hemoglobiini tasot suuret")
    elif hemoglobin_level < 117:
        print("hemoglobiini tasot alhaset")
    else:
        print("hemoglobiini tasot normaali")

else:
    print("Virheellinen sukupuoli")