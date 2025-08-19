kuhan_pituus = float(input("Kuinka pitkä kalastamasi kuha on?: "))
alamittainen_kuha_pituus = 37

if(kuhan_pituus < alamittainen_kuha_pituus):
    pituuden_erotus = alamittainen_kuha_pituus - kuhan_pituus
    print(f"Kalastamanne kuha on {pituuden_erotus:.2f} cm liian lyhyt, laita kuha takaisin järveen")

print("Hyvää päivän jatkoja!")