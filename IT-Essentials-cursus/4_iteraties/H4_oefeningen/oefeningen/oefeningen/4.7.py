#**Oefening 4.7**

#Lees via het toetsenbord de temperatuur gemeten om 12u ’s middags in van 10 dagen.
#Gevraagd een afdruk van
#+	de hoogste temperatuur voor deze 10 dagen
#+	de gemiddelde temperatuur voor deze 10 dagen

#temperatuur =int(input("geef de temperatuur gemeten om 12u ’s middags"))

i = 1
hoogste_temperatuur = 0
sum_temperatuur = 0
while i != 11:
    temperatuur = int(input("geef de temperatuur gemeten om 12u ’s middags in dag " + str(i) + ": "))
    if temperatuur > hoogste_temperatuur:
        hoogste_temperatuur = temperatuur
    sum_temperatuur += temperatuur

    i += 1

print("de hoogste temperatuur voor deze 10 dagen ", hoogste_temperatuur)
print("de gemiddelde temperatuur voor deze 10 dagen ", sum_temperatuur/10)
