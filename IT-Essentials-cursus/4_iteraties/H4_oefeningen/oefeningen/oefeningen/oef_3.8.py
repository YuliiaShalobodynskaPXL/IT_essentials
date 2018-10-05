#opdracht 4.8: Schrijf een programma dat alle getallen
#tussen 0 en 10000 afdrukt die deelbaar zijn door 6 en
#door 28.

for i in range(28,10000, 28):
    if i % 6 == 0 and i % 28 == 0:
        print(i)