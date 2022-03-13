# import
import turtle
import random
t = turtle.Turtle()

colours = ["red", "yellow", "blue", "black", "Green", "purple", "pink"]
for a in range(100):
    t.forward(random.randint(20, 100))
    t.begin_fill()
    t.color(random.choice(colours))
    t.circle(random.randint(10, 100))
    t.end_fill()
    t.right(random.randint(1, 359))

