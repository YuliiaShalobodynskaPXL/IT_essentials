import turtle

wn = turtle.Screen()
alex = turtle.Turtle()

print("Enter a value of X (at least three)")
x = int(input())

alex.left(45)
for i in range(x):
    alex.forward(50)
    alex.left(45)

wn.mainloop()