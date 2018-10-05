
aantal = 1
totale_leeftijd = 0
while aantal <= 10:
    leeftijd = int(input('geef de leeftijd van student ' + str(aantal)))
    totale_leeftijd += leeftijd
    aantal += 1
print("Gemmidelde leeftijd van studenten is ", totale_leeftijd / 10)