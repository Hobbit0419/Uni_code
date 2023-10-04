import turtle as turt


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

#Skapar en turtle som ritar ett pentagram med den översta spetsen i punkten x,y och angiven sidlängd. En fyllnads färg kan också anges
def pentagram(x, y, side, colour):
    pen = make_turtle(x, y)
    pen.speed(0)
    pen.hideturtle()
    pen.setheading(270 - 36/2)
    pen.fillcolor(colour)
    pen.begin_fill()
    for i in range(5):
        pen.forward(side)
        pen.left(180 - 36)
    pen.end_fill()

#Skapar en turtle som ritar tricoloren med nedre vänstra hörnet i punkten x,y och höjden h
#Bredden blir en funktion av höjden då de ska ha ett fast förhållande på 2:3
def tricolore(x, y, h):
    s = 0
    for colour in ['green', 'white', 'orange']:
        rectangle((x + (s*(h/2))), y, h/2 , h, colour)
        s += 1

#Koden nedan ritar bilden som uppgiften efterfrågar, den är också helt skalbar med avseende på tricolorens höjd, ritas alltid centrerad kring origo. 
h = 100
x = 32
y = 32
s = h/2
offset = 2*h/3

tricolore(x-(2*h)/3, y-h/2, h)

for i in range(10):
    if i < 5:
        pentagram(x-(11*h/12) + i*s, y + h/2 + offset, s, 'yellow')
    else:
        pentagram(x-(11*h/12) + (i-5)*s, y -(h/2 + (offset - s)), s, 'yellow')

#ser till att fönstret inte stängs direkt efter det är färdig ritat.
turt.mainloop()