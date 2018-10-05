a = int(input("geef a: "))
b = int(input("geef b: "))
c = int(input("geef c: "))

if c == 1:
    print( a, "+", b, " is ", a + b)
elif c == 2:
    print( a, "-", b, " is ", a - b)
elif c == 3:
    print( a, "*", b, " is ", a * b)
elif c == 4:
    print("Kvadraat van ", a, " is ", a ** 2)
elif c == 5:
    print("Kvadraat van ", b, " is ", b ** 2)
else:
    print("Foutive code")