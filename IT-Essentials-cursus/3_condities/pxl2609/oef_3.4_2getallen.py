getal1 = int(input('geef eerste getal'))
getal2 = int(input('geef tweede getal'))

if getal1 < getal2:
    kleinste = getal1
    grootste = getal2
    print("het kleinste getal is ",    )









    print('het kleinste getal is ', getal1)
    print('het kvadraat van het kleinste getal is ', getal1 * getal1)
    if getal1 !=0:
        print('het grootste getal gedeeld door het kleinste getal is ', getal2 / getal1)
    else:
        print('deling door 0!')
elif getal1 > getal2:
    print('het kleinste getal is ', getal2)
    print('het kvadraat van het kleinste getal is ', getal2 * getal2)
    if getal2 !=0:
        print('het grootste getal gedeeld door het kleinste getal is ', getal1 / getal2)
    else:
        print('deling door 0!')