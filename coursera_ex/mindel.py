n = int(input())
now = 2
while now <= n:
    if n % now != 0:
        now = now + 1
    else:
        delMin = now
print(delMin)