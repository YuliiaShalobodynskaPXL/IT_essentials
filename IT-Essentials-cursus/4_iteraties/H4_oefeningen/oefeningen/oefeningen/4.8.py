#**Oefening 4.8**

#Er wordt door renners een tijdrit gereden over een afstand van 36 km.
#Van iedere renner wordt inschrijvingsnummer en zijn tijd in seconden gegeven. Deze gegevens dienen ingegeven te worden. De invoer stopt wanneer er voor het inschrijvingsnummer een negatief getal wordt ingegeven.
#We veronderstellen dat alle renners er een verschillende tijd over doen.
#Gevraagd:
#+ 	Welke renner is het snelst?
#+ 	Het percentage van de renners dat er langer dan 1 uur over doet?
#Zorg voor volgende afdruk:
#+ 	Snelste renner is de renner met inschrijvingsnummer: .........
#+ 	Het percentage van de renners dat er langer dan 1 uur over doet :………
#**Extra:** Geef van de snelste renner ook zijn tijd in uren, minuten en seconden. En druk dit ook af.

nummer = int(input("geef inschrijvingsnummer: "))

snelste_tijd = 99999999999999
snelst_nummer = 0
hoeveelheid_langer_1_uur = 0
hoeveelheid = 0

while nummer >= 0:
    tijd_sec = int(input("geef tijd in seconden: "))


    if tijd_sec < snelste_tijd:
        snelste_tijd = tijd_sec
        snelst_nummer = nummer
    if tijd_sec > 3600:
        hoeveelheid_langer_1_uur +=1
    hoeveelheid += 1
    nummer = int(input("geef inschrijvingsnummer: "))
   # tijd_sec = int(input("geef tijd in seconden: "))

print()
print("Snelste renner is de renner met inschrijvingsnummer: ", snelst_nummer)
print("Het percentage van de renners dat er langer dan 1 uur over doet : ", round(hoeveelheid_langer_1_uur * 100 / hoeveelheid))

beste_uur = snelste_tijd // 3600
beste_min = snelste_tijd % 3600 // 60
beste_sec = snelste_tijd - beste_uur * 3600 - beste_min * 60

print("Beste resultat is: ", beste_uur , " uur, ", beste_min, " minuten, ", beste_sec, " seconden.")
