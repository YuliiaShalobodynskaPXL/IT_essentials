exam1 = int(input('geef resultat van examen 1 '))
exam2 = int(input('geef resultat van examen 2 '))
exam3 = int(input('geef resultat van examen 3 '))

resultat = (exam1 + exam2 + exam2) * 100 / 60

if resultat < 60:
    print('onvoldoende')
elif resultat < 70:
    print('voldoende')
elif resultat < 80:
    print('onderscheiding')
elif resultat < 90:
    print('grote onderscheiding')
else:
    print('grotste onderscheiding')