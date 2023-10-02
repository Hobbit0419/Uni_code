import turtle as turt
from math import sqrt
from math import sin
from math import cos
from math import pi



def jump(x, y, turtle):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

#Skapar en turtle och flyttar den till punkten x,y utan att rita <=> skapar en turtle i punkten x,y
def make_pen(x, y):
    pen = turt.Turtle()
    jump(x, y, pen)
    pen.hideturtle
    pen.speed(0)
    return pen

def stickman(x, y, h):
    pen = make_pen(x, y)
    pen.circle(h/8)
    head = pen.pos()
    pen.setheading(-90)
    pen.forward(2*h/3)
    pos = pen.pos()
    pen.left(45)
    pen.forward(sqrt((h/3)**2 + (h/6)**2))
    jump(pos[0], pos[1], pen)
    pen.right(90)
    pen.forward(sqrt((h/3)**2 + (h/6)**2))
    jump(head[0], head[1], pen)
    pen.setheading(-90)
    pen.forward(2*h/6)
    pos = pen.pos()
    pen.setheading(90)
    pen.left(45)
    pen.forward(sqrt((h/3)**2 + (h/6)**2))
    jump(pos[0], pos[1], pen)
    pen.right(90)
    pen.forward(sqrt((h/3)**2 + (h/6)**2))

def balistic_arc(x, y, v0, theta, tstep):
     pen =  make_pen(x ,y)
     t = 0
     X = v0*cos(theta)*t
     Y = v0*sin(theta)*t - (9.82*t**2)/2
     while Y >= 0:
         X = v0*cos(theta)*t
         Y = v0*sin(theta)*t - (9.82*t**2)/2
         pen.goto(X, Y)
         t += tstep

         
turt.mainloop()


    
