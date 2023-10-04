import turtle as turt
from random import randint
from math import atan
from math import pi

#Flytta turtlen till en punkt x,y utan att rita
def jump(x, y, turtle):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

#Skapar en turtle och flyttar den till punkten x,y utan att rita <=> skapar en turtle i punkten x,y
def make_turtle(x, y):
    t = turt.Turtle()
    jump(x, y, t)
    return t

#Skapar en turtle som ritar en rektangel med nedre vänstra hörnet i punkten x,y med angiven höjd, bredd och fyllnads färg
def rectangle(x, y, width, height, colour):
    pen = make_turtle(x, y)
    pen.speed(0)
    pen.hideturtle()
    pen.fillcolor(colour)
    pen.begin_fill()
    for length in [width, height, width, height]:
        pen.fd(length)
        pen.left(90)
    pen.end_fill()

def move_random(t):
    heading_0 = (atan(t.ycor()/t.xcor())*(180/pi))
    
    if not -250 < t.xcor() < 250:
        t.setheading(heading_0)
        t.forward(randint(0,25))
        print(t.heading(), heading_0)
    elif not -250 < t.ycor() < 250:
        t.setheading(heading_0)
        t.forward(randint(0,25))
        print(t.heading(), heading_0)
    else:
        t.right(randint(-45,45))
        t.forward(randint(0,25))
        print(t.heading(), heading_0)
   

rectangle(-250,-250,500,500,'lightblue')
pen = make_turtle(randint(-250,250), randint(-250,250))

for i in range(250):
    move_random(pen)

turt.mainloop()