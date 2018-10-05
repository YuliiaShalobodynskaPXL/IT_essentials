BTW_FACTOR = 1.21

prijs = 11.5
hoeveelheid = int(input('hoeveel articles wil je bestelen? '))
totale_prijs = prijs * BTW_FACTOR * hoeveelheid

if totale_prijs > 1000:
    print('te betalen: ', totale_prijs * 0.9)
else:
    print('te betalen: ', totale_prijs)