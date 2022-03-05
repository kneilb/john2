import turtle

t = turtle.Turtle()

t.shape("turtle")

for s in range(100):
    t.left(50)
    for i in range(4):
        t.forward(100)
        t.left(90)

t.color("red")
t.color("yellow")

t.left(90)
