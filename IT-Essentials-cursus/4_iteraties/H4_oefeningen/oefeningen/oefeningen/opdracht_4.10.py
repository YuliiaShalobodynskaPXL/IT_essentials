#**Oefening 4.10**

#Schrijf een programma om volgende schermafdruk te verkrijgen.
#![alt-text](.\images\pyramide.jpg "Oefening 10")
#De grootte van de driehoek wordt als gegeven via het toetsenbord ingegeven.
#Ter info: de hoogte en de breedte van de driehoek zijn gelijk

grotte_van_driehoek = int(input("geef de grotte van de driehoek: "))
max = grotte_van_driehoek + 1

for i in range(max):
    for j in range(max-i, 1, -1):
        print("@ ", end="")
    print()