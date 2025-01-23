import random
import time
import turtle


def polygon(t, sides, length):
    angle = 360 / sides
    for _ in range(sides):
        t.forward(length)
        t.left(angle)

colours = ["red", "green", "blue", "yellow", "orange", "pink", "black"]
shapes = [3, 4, 5, 6, 8, 10]

t = turtle.Turtle()
t.shape("turtle")

for _ in range(5):
    colour = random.choice(colours)
    sides = random.choice(shapes)
    length = random.randint(30, 50)

    t.fillcolor(colour)

    t.begin_fill()
    polygon(t, sides, length)
    t.end_fill()

    t.left(random.randint(0, 360))
    t.forward(100)


while(True):
    time.sleep(10)