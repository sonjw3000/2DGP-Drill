import turtle as t

t.penup()
t.goto(-300,300)

for i in range(6):
    t.goto(-300, + 300 + i * -100)
    t.pendown()
    t.forward(500)

    t.penup()
    t.goto(-300 + i * + 100, 300)
    t.right(90)

    t.pendown()
    t.forward(500)
    t.left(90)
    t.penup()

t.exitonclick()