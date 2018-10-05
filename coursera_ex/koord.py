x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x1 > 0:
    signX1 = 1
else:
    signX1 = -1
if y1 > 0:
    signY1 = 1
else:
    signY1 = -1
if x2 > 0:
    signX2 = 1
else:
    signX2 = -1
if y2 > 0:
    signY2 = 1
else:
    signY2 = -1
if signX1 == signX2 and signY1 == signY2:
    print('Yes')
else:
    print('No')
