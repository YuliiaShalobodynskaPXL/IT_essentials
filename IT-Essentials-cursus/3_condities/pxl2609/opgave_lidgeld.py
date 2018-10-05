Leeftijd = int(input('geef je leeftijd'))
Burgelijke_staat = int(input('geef je burgelijke staat(1-2-3)'))

#a: ongehuud : 25 e; gehuwd ; 20 e; weduw : 15e

if Burgelijke_staat == 1:
    print('berekening a. lidgeld :25')
elif Burgelijke_staat == 2:
    print('berekening a. lidgeld :20')
else:
    print('berekening a. lidgeld :15')

#b: ongehuud jonger dan 30: 25 e; gehuwd ; alle overige betalen 15e

if Burgelijke_staat == 1 and Leeftijd < 30:
    print('berekening b. lidgeld :25')
else:
    print('berekening b. lidgeld :15')

#c: alle leden jonger dan 30 en alle ongehuwde: 25 e;
    #  alle overige betalen 15e

if Leeftijd < 30 or Burgelijke_staat == 1:
    print('berekening c. lidgeld :25')
else:
    print('berekening c. lidgeld :15')

#c: ongehuwde: 25 e; gehuwd jonger dan 30 : 20e;
    #  alle overige betalen 15e

if Burgelijke_staat == 1:
    print('berekening d. lidgeld :25')
elif Leeftijd < 30 and Burgelijke_staat == 2:
    print('berekening d. lidgeld :20')
else:
    print('berekening d. lidgeld :15')