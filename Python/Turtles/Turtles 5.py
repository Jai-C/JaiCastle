import turtle
import random

wn = turtle.Screen()
alex = turtle.Turtle()
bob = turtle.Turtle()
alex.speed(0)
bob.speed(0)
alex.sety(-400)
for i in range(10000):
    alex.circle(i)
    alex.color('black')
    if random.randint(1,100) % 5 ==0:
        alex.color('green')
