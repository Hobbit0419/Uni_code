import turtle as turt

#Flytta turtlen till en punkt x,y utan att rita
def jump(x, y, turtle):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()

#Skapar en turtle och flyttar den till punkten x,y utan att rita <=> skapar en turtle i punkten x,y
def make_turtle(x = 0, y = 0):
    t = turt.Turtle()
    t.hideturtle()
    jump(x, y, t)
    return t

#Skapar en turtle som ritar en rektangel med nedre vänstra hörnet i punkten x,y med angiven höjd, bredd och fyllnads färg
def rectangle(x = 0, y = 0, width = 100, height = 100, colour = ''):
    pen = make_turtle(x, y)
    pen.speed(0)
    pen.hideturtle()
    pen.color(colour)
    pen.fillcolor(colour)
    pen.begin_fill()
    for length in [width, height, width, height]:
        pen.fd(length)
        pen.left(90)
    pen.end_fill()

#Skapar en turtle som ritar ett pentagram med den översta spetsen i punkten x,y och angiven sidlängd. En fyllnads färg kan också anges
def pentagram(x = 0, y = 0, side = 50, colour = ''):
    pen = make_turtle(x, y)
    pen.color(colour)
    pen.speed(0)
    pen.hideturtle()
    pen.setheading(270 - 36/2)
    pen.fillcolor(colour)
    pen.begin_fill()
    for i in range(5):
        pen.forward(side)
        pen.left(180 - 36)
    pen.end_fill()

#Ritar den vietnamesiska flaggan
def vietnamese_flag(x = 0, y = 0, height = 100):
    rectangle(x, y, height, 2*height/3,'red')
    pentagram(x + height/2, y + height/2,height/3, 'yellow')

vietnamese_flag(-100,-100)

#Jag har valt att lägga default värden i alla funktioner där det är relevant för att jag kunde det
turt.mainloop()