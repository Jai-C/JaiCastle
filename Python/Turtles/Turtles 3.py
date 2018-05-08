import turtle

wn = turtle.Screen
alex = turtle.Turtle()

alex.speed(0)

for i in range(1000):
    alex.forward(i/5)
    alex.left(i*0.2)
    alex.back(i/5)
    alex.right(i/0.5)