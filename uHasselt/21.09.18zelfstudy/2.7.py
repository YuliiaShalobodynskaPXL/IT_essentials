print("enter X")
x = str(input())
for i in range(11):
    lengt_max = len(10*x)
    l = lenght_max - len(i)
    print(x, " times ", i, " = ",""*l, i*x)