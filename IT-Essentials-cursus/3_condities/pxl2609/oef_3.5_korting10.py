BTW_FACTOR = 1.21

prijs = 11.5
hoeveelheid = int(input('hoeveel articles wil je bestelen? '))

if prijs * BTW_FACTOR * hoeveelheid > 1000:
    print('te betalen: ', prijs * BTW_FACTOR * hoeveelheid * 0.9)
else:
    print('te betalen: ', prijs * BTW_FACTOR * hoeveelheid)