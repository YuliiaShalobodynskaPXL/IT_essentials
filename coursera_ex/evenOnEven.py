a = int(input())
b = int(input())
c = int(input())
if a % 2 == 0:
    xA = 0
else:
    xA = 1
elif b % 2 == 0:
    xB = 0
else:
    xB = 1
elif c % 2 == 0:
    xC = 0
else:
    xC = 1
elif xA + xB + xC == 0 or xA + xB + xC == 3:
    print('No')
else:
    print('Yes')
