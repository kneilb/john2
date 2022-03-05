import turtle

def square(t, length=100):
    for i in range(4):
        t.forward(length)
        t.left(90)

def pentagon(t, length=100):
    polygon(t, 5, length)

def hexagon(t, length=100):
    polygon(t, 6, length)

def polygon(t, sides, length=100):
    angle = int(360 / sides)
    for _ in range(sides):
        t.forward(length)
        t.left(angle)


t = turtle.Turtle()

t.shape("turtle")

change = 15
iterations = int(360 / change)

for i in range(iterations):
    # square(t)
    hexagon(t)
    # polygon(t, 7)
    t.left(change)
