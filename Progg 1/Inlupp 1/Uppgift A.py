import turtle as turt


#Flytta turtlen till en punkt x,y utan att rita
def jump(x, y, turtle):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

#Skapar en turtle och flyttar den till punkten x,y utan att rita <=> skapar en turtle i punkten x,y
def make_turtle(x = 0, y = 0):
    t = turt.Turtle()
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

#Skapar en turtle som ritar ett pentagram med den översta spetsen i punkten x,y och angiven sidlängd. En fyllnads färg kan också anges
def pentagram(x = 0, y = 0, side = 50, colour=''):
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
def tricolore(x = 0, y = 0, h = 100):
    s = 0
    for colour in ['red', 'white', 'blue']:
        rectangle((x + (s*(h/2))), y, h/2 , h, colour)
        s += 1

#Funktionen ritar bilden som uppgiften efterfrågar, finns säkert bättre sätt att rita stjärnorna på men kom inte på någon effektivare lösning, offset variabeln kommer från uppskattning i bilden som fanns i uppgiften
def uppgiftA(height = 100, x = 0, y = 0):
    s = height/2
    offset = 2*height/3

    tricolore(x-(2*height)/3, y-height/2, height)

    for i in range(10):
        if i < 5:
            pentagram(x-(11*height/12) + i*s, y + height/2 + offset, s, 'yellow')
        else:
            pentagram(x-(11*height/12) + (i-5)*s, y -(height/2 + (offset - s)), s, 'yellow')


uppgiftA()
#ser till att fönstret inte stängs direkt efter det är färdig ritat.
turt.mainloop()