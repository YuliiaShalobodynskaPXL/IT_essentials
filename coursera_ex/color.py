a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a % 2 == 0 and b % 2 == 0) or (a % 2 != 0 and b % 2 != 0):
    color1 = 1
else:
    color1 = 2
if (c % 2 == 0 and d % 2 == 0) or (c % 2 != 0 and d % 2 != 0):
    color2 = 1
else:
    color2 = 2
if color1 == color2:
    print('Yes')
else:
    print('No')
