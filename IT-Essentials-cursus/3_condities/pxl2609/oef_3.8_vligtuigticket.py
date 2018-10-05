afstand = int(input("geef afstand in km: "))
klasse = int(input("geef de klasse(1 - toerist, 2 - charter, 3 - business): "))

if afstand < 1000:
    prijs = 25 * afstand
elif afstand <= 2999:
    prijs = 20 * afstand
else:
    prijs = 12 * afstand

if klasse == 2:
    prijs = prijs * 0.8
elif klasse == 3:
    prijs = prijs * 1.3

print("De prijs van de vliegtugticket is ", prijs // 100, " euro", prijs % 100, " cents")

