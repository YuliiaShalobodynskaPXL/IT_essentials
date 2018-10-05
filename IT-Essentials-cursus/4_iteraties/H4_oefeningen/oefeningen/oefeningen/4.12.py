'''**Oefening 4.12**

Een onderneming wenst aan haar personeelsleden een premie uit te betalen die in verhouding staat tot het aantal
 dienstjaren. Bereken de individuele premie en de totale premie. Per personeelslid dient via het toetsenbord het
 volgende ingegeven te worden: de familienaam (invoer van "/" of "\*" betekent het einde van het programma),
 voornaam en het aantal dienstjaren. Zorg voor een invoercontrole op het aantal dienstjaren, dit moet een getal zijn
 tussen 0 en 40 jaar.  De premie wordt als volgt berekend: het aantal dienstjaren * 25 euro. Als het aantal dienstjaren
  minder zijn dan 5, krijgt de persoon 0 euro als premie. Druk per persoon de familienaam, de voornaam, het aantal jaren
  dienst en de premie af.  Druk aan het einde van het programma de totaal te betalen premie en de hoogste premie af.'''


familienaam = str(input("geef familienaam: "))

premie = 0
totaal_te_betalen = 0
hoogste_premie = 0
while familienaam != "/" and familienaam != "*":
    naam = str(input("geef voornaam "))
    jaren = int(input("geef het aantal dienstjaren: "))
    if jaren > 0 and jaren < 40:
        if jaren > 4:
            premie = jaren * 25
            totaal_te_betalen += premie
            if premie > hoogste_premie:
                hoogste_premie = premie
    else:
        jaren = int(input("Fout! Het aantal dienstjaren moet tussen 0 en 40 zijn.Geef het aantal dienstjaren: "))
        if jaren > 4:
            premie = jaren * 25
            totaal_te_betalen += premie
            if premie > hoogste_premie:
                hoogste_premie = premie
    print()
    print("De familienaam: ", familienaam, "De voornaam: ", naam, "Het aantal jaren in dienst: ", jaren, "De PREMIE: ",
          premie)
    print()
    familienaam = str(input("geef familienaam: "))
print()
print('de totaal te betalen premie: ', totaal_te_betalen)
print('de hoogste premie: ', hoogste_premie)


