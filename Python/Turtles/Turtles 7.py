import turtle
import random

wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(0)
for i in range(1000):
    n = 1
    while n < 100:
        alex.circle(n*(i+1))
        n = n * 1.2