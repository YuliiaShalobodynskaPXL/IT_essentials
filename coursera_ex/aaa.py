a = int(input())
b = int(input())
c = int(input())
if a % 2 == 0:
    x = 0
elif a % 2 != 0:
    x = 1
elif b % 2 == 0:
    y = 0
elif b % 2 != 0:
    y = 1
elif c % 2 == 0:
    z = 0
elif c % 2 != 0:
    z = 1
print(x + y + z)
elif (x + y + z == 0) or (x + y + z == 3):
    print('No')
else:
    print('Yes')
