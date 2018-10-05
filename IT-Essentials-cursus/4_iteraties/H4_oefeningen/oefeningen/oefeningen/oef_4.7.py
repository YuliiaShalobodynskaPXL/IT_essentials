#opdracht 4.7: Schrijf een programma dat alle getallen
#tussen -10 en +10 afdrukt. Voeg bij de positieve
#getallen het “+”teken. (0 heeft geen teken).

for i in range(-9, 10):
    if  i > 0:
        print("+" + str(i))
    else:
        print(i)
    