gewicht = float(input('geef je gewicht'))
lengte  = float(input('geef je lengte'))
bmi = gewicht /(lengte * lengte)
if bmi < 18:
    print('ondergewicht')
elif bmi < 25:
    print('ok')
elif bmi < 30:
    print('overgewicht')
elif bmi < 40:
    print('obesitas')
else:
    print('ziekelijke overgewicht')
print('tot ziens')