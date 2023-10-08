import turtle as turt
from random import randint
from math import atan
from math import pi
from math import sqrt


#Flytta turtlen till en punkt x,y utan att rita
def jump(x, y, turtle):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


#Skapar en turtle och flyttar den till punkten x,y utan att rita <=> skapar en turtle i punkten x,y
def make_turtle(x, y, colour=''):
    t = turt.Turtle()
    t.color(colour)
    jump(x, y, t)
    return t


#Skapar en turtle som ritar en rektangel med nedre vänstra hörnet i punkten x,y med angiven höjd, bredd och fyllnads färg
def rectangle(x, y, width, height, colour=''):
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
        t.setheading(t.towards(0, 0))
        t.forward(randint(0, 25))
    elif not -250 < t.ycor() < 250:
        t.setheading(t.towards(0, 0))
        t.forward(randint(0, 25))      
    else:
        t.right(randint(-45, 45))
        t.forward(randint(0, 25))


def two_turtles(colour1 = 'red', colour2 = 'green', background_colour = 'gray', size = 500, cycles = 100):
    rectangle(-size/2,-size/2,size,size,background_colour)
    green = make_turtle(randint(-250,250), randint(-250,250), colour2)
    red = make_turtle(randint(-250,250), randint(-250,250), colour1)
    close_count = 0

    for i in range(cycles):
        if sqrt((red.ycor() - green.ycor())**2 + (red.xcor() - green.xcor())**2) < 50:
            red.write('close')
            close_count += 1
            move_random(red)
            move_random(green)
        else:
            move_random(red)
            move_random(green)
    return close_count

count = two_turtles()
print(count)
turt.mainloop()