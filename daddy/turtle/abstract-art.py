import turtle
import random

COLOURS = ["red", "green", "blue", "pink", "orange", "black", "yellow"]


def polygon(t, sides, length):
    angle = int(360 / sides)
    for _ in range(sides):
        t.forward(length)
        t.left(angle)


def square(t, length):
    polygon(t, 4, length)


t = turtle.Turtle()
t.shape("turtle")

for i in range(100):
    t.begin_fill()
    t.color(random.choice(COLOURS))
    side_length = random.randint(10, 50)
    square(t, side_length)
    t.end_fill()

    move_distance = random.randint(30, 100)
    t.forward(move_distance)

    turn_angle = random.randint(0, 90)
    t.left(turn_angle)

    t.begin_fill()
    t.color(random.choice(COLOURS))
    radius = random.randint(5, 30)
    t.circle(radius)
    t.end_fill()
