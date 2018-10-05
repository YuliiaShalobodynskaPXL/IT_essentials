#opdracht 4.1: In een klas zitten 5 studenten.
#Bereken de gemiddelde leeftijd van deze
#studenten. Hoe?
# opdracht 4.2: Zelfde opgave maar met 28
#studenten. Hoe?


totale_leeftijd = 0

for i in range(1,11):
    leeftijd = int(input("geef de leeftijd van student " + str(i) + ":"))   # dla input tolko +, zapjatuju ispolzovay NELZJA!
    totale_leeftijd += leeftijd

print("gemiddelde leeftijd is ", totale_leeftijd / i)
