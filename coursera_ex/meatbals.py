k = int(input())
m = int(input())
n = int(input())
if k == 1:
    print(2 * n * m)
elif n > k and n % k != 0:
    print((2 * n + k) // k * m)
elif n > k and n % k == 0:
    print(2 * n // k * m)
else:
    print(2*m)
