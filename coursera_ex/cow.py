a = int(input())
if a % 10 == 1 and a != 11:
    print(a, ' korova')
elif 2 <= a % 10 <= 4 and a != 12 and a != 13 and a != 14:
    print(a, ' korovy')
else:
    print(a, ' korov')
