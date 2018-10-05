#er wordt altijd lijn per lijn gedrukt
#en binnen 1 lijn worden de details gedrukt

for lijn in range(1,6):
    for kolom in range(1,11):
        getal = lijn * kolom
        print(str(getal) + "\t", end = "")
    print()