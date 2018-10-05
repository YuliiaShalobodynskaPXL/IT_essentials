x = int(input())
y = int(input())

for i in range(y):
    for j in range(x):
        j = j + 1
        print(j, end = " ")
    print()
    i = (y - 2)*x + 1
    print(i, end = " ")
