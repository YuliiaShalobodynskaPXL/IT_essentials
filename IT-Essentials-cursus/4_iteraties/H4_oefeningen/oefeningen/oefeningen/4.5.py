




getal = int(input('geef een getal tussen 1 en 100'))
while getal <= 1 or getal >= 100:
    if getal <= 1:
        print("Fout! het getal moet groter dan 1 zijn")
    else:
        print("Fout! het getal moet kleiner dan 100 zijn")
    getal = int(input('geef een getal tussen 1 en 100'))
print('Het juiste getal ', getal)

