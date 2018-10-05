a = int(input())
b = int(input())
c = int(input())
if a > b + c:
    print('impossible')
elif a**a == b**b + c**c:
    print('rectangular')
elif b**b == a**a + c**c:
    print('rectangular')
elif c**c == a**a + b**b:
    print('rectangular')
elif a**a > b**b + c**c:
    print('obtuse')
elif b**b > a**a + c**c:
    print('obtuse')
elif c**c > a**a + b**b:
    print('obtuse')
else:
    print('acute')
