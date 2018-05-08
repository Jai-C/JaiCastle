import turtle
wn = turtle.Screen()
alex = turtle.Turtle()
alex.speed(0)

##for i in range(20000):
##    for n in range(10):
##        alex.forward(i*5)
##        alex.right(n*10)
##        for m in (0.5,1):
##            if m == 1:
##                alex.forward(i*n*m)

    
for n in range(0,10000000,1):
    alex.forward(n)
    for i in range(10):
        alex.left(n*i)
