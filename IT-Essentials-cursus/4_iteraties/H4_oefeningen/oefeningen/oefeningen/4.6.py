#**Oefening 4.6**

#Geef via het toetsenbord artikelnummer, hoeveelheid en eenheidsprijs in. De invoer eindigt met artikelnummer = 999. Gevraagd een afdruk van:
#+ de gegevens per artikel (artikelnummer, hoeveelheid, eenheidsprijs, bedrag)
#+ het totaal te betalen bedrag van de aankoop.

artikelnummer = int(input("geef artikelnummer: "))


totaal_te_betalen = 0

while artikelnummer != 999:
    hoeveelheid = int(input("geef hoeveelheid : "))
    eenheidsprijs = int(input("geef eenheidsprijs: "))
    print()
    print("Artikelnummer: ", artikelnummer)
    print("Hoeveelheid: ", hoeveelheid)
    print("Eenheidsprijs: ", eenheidsprijs)
    print()
    totaal_te_betalen += hoeveelheid * eenheidsprijs
    artikelnummer = int(input("geef artikelnummer: "))

print()
print("Het totaal te betalen :", totaal_te_betalen)