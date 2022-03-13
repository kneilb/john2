import turtle
import random
import time

t = turtle.Turtle()
# house code
def house(x, y):
    t.penup()
    t.goto(x, y)
    t.color("orange")
    t.setheading(0)
    t.pendown()
    t.begin_fill()
    size = random.randint(30, 50)
    for a in range(4):
        t.forward(size)
        t.left(90)
    t.end_fill()
    t.left(90)
    t.forward(size)
    t.left(90)
    overhang = random.randint(5, 10)
    t.forward(overhang)
    roof_length = 2 * overhang + size
    t.color("brown")
    t.begin_fill()
    for a in range(3):
        t.right(120)
        t.forward(roof_length)
    t.end_fill()

# main code
for a in range(10):
    house(random.randint(-200, 200), random.randint(-200, 200))

while True:
    time.sleep(10)
