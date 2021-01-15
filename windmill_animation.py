import turtle
win = turtle.Screen()
win.setup(600, 600)

t1 = turtle.Turtle()
t2 = turtle.Turtle()
t3 = turtle.Turtle()

t1.hideturtle()
t2.hideturtle()
t3.hideturtle()

t1.color('red')

t1.pensize = 2
t2.pensize = 2
t3.pensize = 2


t1.speed(0)
t2.speed(0)
t3.speed(0)


animate = 1


def rect(t2):
    t2.forward(120)
    t2.left(90)
    t2.forward(20)
    t2.left(90)
    t2.forward(120)



def design(t1, t2, t3, angle):

    t1.color('red')
    t1.setpos(0, 0)
    t1.circle(20)

    t2.color('blue')
    t2.penup()
    t2.circle(20, -30 + angle)
    t2.right(60)
    t2.pendown()
    rect(t2)
    t2.penup()
    t2.forward(35)
    t2.pendown()
    t2.pendown()
    rect(t2)

    t3.color('blue')
    t3.penup()
    t3.circle(20, 60 + angle)
    t3.right(60)
    t3.pendown()
    rect(t3)
    t3.penup()
    t3.forward(35)
    t3.pendown()
    t3.pendown()
    rect(t3)

    t2.penup()
    t3.penup()
    t2.goto(0, 0)
    t2.setheading(0)
    t3.goto(0, 0)
    t3.setheading(0)
    t2.pendown()
    t3.pendown()

    t1.hideturtle()
    t2.hideturtle()
    t3.hideturtle()

    if animate:
        win.update()

if animate:
    win.tracer(0, 0)

Rounds = 20
time_in_ms = 300
for i in range(0, (Rounds*360), 10):
    win.ontimer(design(t1, t2, t3, i), time_in_ms)
    win.reset()

win.listen()
win.mainloop()
