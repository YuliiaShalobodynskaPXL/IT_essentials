HUDIG_JAAR = 2018
jaar = int(input('geef van welke jaar de film is '))
rating = int(input('geef rating(1-5) '))
basisprijs = 5

if HUDIG_JAAR - jaar < 2:
    prijs = basisprijs + 1
if rating >= 4:
    prijs = basisprijs + 2
elif jaar < 2:
    prijs = basisprijs + 1
else:
    prijs = basisprijs

print('Prijs ', str(prijs), 'euro')