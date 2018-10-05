#gewicht_op_aarde = int(input('geef het gewicht'))

percentage_MAAN = 0.165
percentage_JUPITER = 2.537
percentage_MARS = 0.378

for i in range(50, 121, 5):
    print("Aarde:", i)
    print("Maan:", i * percentage_MAAN)
    print("Jupiter:",i * percentage_JUPITER)
    print("Mars:",i * percentage_MARS)
    print()