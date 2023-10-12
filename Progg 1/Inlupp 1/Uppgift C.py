import turtle as turt
from random import randint
from math import sqrt


#Flytta turtlen till en punkt x,y utan att rita
def jump(x, y, turtle):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

#Skapar en turtle och flyttar den till punkten x,y utan att rita <=> skapar en turtle i punkten x,y
def make_turtle(x = 0, y = 0, colour = ''):
    t = turt.Turtle()
    t.color(colour)
    jump(x, y, t)
    return t

#Skapar en turtle som ritar en rektangel med nedre vänstra hörnet i punkten x,y med angiven höjd, bredd och fyllnads färg
def rectangle(x = 0, y = 0, width = 100, height = 100, colour = ''):
    pen = make_turtle(x, y)
    pen.speed(0)
    pen.hideturtle()
    pen.fillcolor(colour)
    pen.begin_fill()
    for length in [width, height, width, height]:
        pen.fd(length)
        pen.left(90)
    pen.end_fill()

#Funktionen tar en turtle som argument och flyttar denna i en slumpmässig riktning ett slumpmässigt avstånd. Man kan också mata in xbound och ybound för att sätta ett område som turtlen inte kan lämna
def move_random(t, xbound = 500, ybound = 500):
    if not -xbound/2 < t.xcor() < xbound/2 or not -ybound/2 < t.ycor() < ybound/2: #kollar så turtlen är innanför gränserna
        t.setheading(t.towards(0, 0))
        t.forward(randint(0, 25))
    else:
        t.right(randint(-45, 45))
        t.forward(randint(0, 25))

#Funktionen skapar två turtles, ritar en ruta och flyttar turtles helt slumpmässigt inom rutan. 
def two_turtles(colour1 = 'red', colour2 = 'green', background_colour = 'gray', xsize = 500, ysize = 500, cycles = 100):
    rectangle(-xsize/2, -ysize/2, xsize, ysize, background_colour)
    green = make_turtle(randint(-xsize/2,xsize/2), randint(-ysize/2, ysize/2), colour2)
    red = make_turtle(randint(-xsize/2,xsize/2), randint(-ysize/2, ysize/2), colour1)
    close_count = 0

    for i in range(cycles):
        if sqrt((red.ycor() - green.ycor())**2 + (red.xcor() - green.xcor())**2) < 50: #denna if sats kollar avståndet mellan turtles och skriver close om dem är närmre än 50 punkter har också en räknare som räknar antalet gånger detta händer
            close_count += 1
            red.write('close')
        else:
            move_random(red, xsize, ysize)
            move_random(green, xsize, ysize)
    print(close_count)
    return close_count

two_turtles()

turt.mainloop()