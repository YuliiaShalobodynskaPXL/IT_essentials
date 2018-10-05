#**Oefening 4.4**

#Van werknemers in een bedrijf wil men de conditie nagaan. Volgende gegevens worden via het toetsenbord
#  ingegeven: het geslacht (1 = man, 2 = vrouw) en de afstand afgelegd in km na 12 minuten lopen. De invoer
#  stopt wanneer er voor geslacht een getal wordt ingegeven dat niet 1 of 2 is. Op basis van de afgelegde
# km kan men het conditiegetal berekenen:
#$conditie\_getal = \frac{(afstand(in\ meter) - 504.9)}{44.73}$

#*Gevraagd:* Geef het percentage van de werknemers die een slechte conditie hebben. We spreken voor vrouwen over
# een slechte conditie als het conditiegetal kleiner is dan 29, voor mannen als het conditiegetal kleiner dan 36 is.

geslacht = int(input('het geslacht (1 = man, 2 = vrouw): '))

antaal_mensen_met_slecht_conditie = 0
antaal_mensen = 0
while geslacht == 1 or geslacht == 2:
    antaal_mensen += 1
    afstand = int(input('de afstand afgelegd in km na 12 minuten lopen: '))
    conditie = (afstand * 1000 - 504.9) / 44.73
    if geslacht == 1 and conditie < 36:
        antaal_mensen_met_slecht_conditie += 1
    elif geslacht == 2 and conditie < 29:
        antaal_mensen_met_slecht_conditie += 1
    geslacht = int(input('het geslacht (1 = man, 2 = vrouw): '))
print()
#print(antaal_mensen_met_slecht_conditie)
#print(antaal_mensen)
print("het percentage van de werknemers die een slechte conditie hebben: ",
      round(antaal_mensen_met_slecht_conditie * 100 / antaal_mensen), "%")
