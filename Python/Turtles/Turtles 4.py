import turtle
import random
wn = turtle.Screen
alex = turtle.Turtle()

alex.speed(0)

for i in range(1000):
    for n in (1,-1):
        if random.randint(0,2) == 1:
            alex.circle(i*n)

input()