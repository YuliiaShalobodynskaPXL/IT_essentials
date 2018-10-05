#**Oefening 4.9**

#Schrijf een programma dat tafels van vermenigvuldiging
# afdrukt voor de getallen 2 tot 5(incl.).

for i in range(2,6):
    for j in range(1, 11):
        print(str(j) + " * " + str(i) +  " = " + str(i * j))
    print()


