from tkinter import *
from copy import copy

import random

# global constants
CANVAS_HEIGHT = 480
CANVAS_WIDTH = 480
CELL_SIZE = 30
CELLS_X = int(CANVAS_WIDTH / CELL_SIZE)
CELLS_Y = int(CANVAS_HEIGHT / CELL_SIZE)
BORDER_X = CANVAS_WIDTH - (CELLS_X * CELL_SIZE)
BORDER_Y = CANVAS_HEIGHT - (CELLS_Y * CELL_SIZE)
MOVE_INTERVAL = 500
SEGMENT_COLOURS = ("green", "red", "yellow")

# global variables
velocity = (0,0)

body = []
sweets = set()


# functions
def out_of_bounds(pos):
    return pos[0] < 0 or \
       pos[1] < 0 or \
       pos[0] >= CELLS_X or \
       pos[1] >= CELLS_Y

def to_canvas_x(x):
    return BORDER_X + CELL_SIZE * x

def to_canvas_y(y):
    return BORDER_Y + CELL_SIZE * y

def spawn_sweet():
    while True:
        sweet_pos = (
            random.randint(0, CELLS_X - 1),
            random.randint(0, CELLS_Y - 1)
        )

        if sweet_pos not in sweets and \
           sweet_pos not in body:
            sweets.add(sweet_pos)
            return

def sweet_present(x, y):
    sweet_pos = (x, y)
    return sweet_pos in sweets

def remove_sweet(x, y):
    sweet_pos = (x, y)
    sweets.remove(sweet_pos)

def add_new_segment(x, y):
    body.insert(0, (x, y))

def remove_last_segment():
    del body[-1]

def draw_segment(x, y, colour):
    canvas.create_oval(
        to_canvas_x(x),
        to_canvas_y(y),
        to_canvas_x(x + 1),
        to_canvas_y(y + 1),
        fill=colour
    )

def draw_sweet(x, y):
    canvas.create_rectangle(
        to_canvas_x(x) + CELL_SIZE / 4,
        to_canvas_y(y) + CELL_SIZE / 4,
        to_canvas_x(x + 1) - CELL_SIZE / 4,
        to_canvas_y(y + 1) - CELL_SIZE / 4,
        fill="red"
    )

def key_event(event):
    global velocity
    k = event.keysym

    if k == "Up":
        velocity = (0, -1)
    elif k == "Down":
        velocity = (0, 1)
    elif k == "Left":
        velocity = (-1, 0)
    elif k == "Right":
        velocity = (1, 0)

    print(f"Velocity is {velocity}")

def move_snake():
    dead = False
    head_pos = body[0]

    new_pos = (
        head_pos[0] + velocity[0],
        head_pos[1] + velocity[1]
    )

    print(head_pos, velocity, "->", new_pos)

    if out_of_bounds(new_pos) or (velocity != (0, 0) and new_pos in body):
        print("crash")
        dead = True

    else:
        add_new_segment(new_pos[0], new_pos[1])

        if sweet_present(new_pos[0], new_pos[1]):
            remove_sweet(new_pos[0], new_pos[1])
            spawn_sweet()
        else:
            remove_last_segment()

    for i in canvas.find_all():
        canvas.delete(i)

    for i, c in enumerate(body):
        colour = "black" if i == 0 else SEGMENT_COLOURS[i % len(SEGMENT_COLOURS)]
        draw_segment(c[0], c[1], colour)

    for s in sweets:
        draw_sweet(s[0], s[1])

    if not dead:
        window.after(MOVE_INTERVAL, move_snake)

################################################################################
##                                   MAIN                                     ##
################################################################################

window = Tk()
window.title("snake!")

canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

add_new_segment(0, 0)
spawn_sweet()

canvas.bind_all("<Key>", key_event)

window.after(MOVE_INTERVAL, move_snake)
window.mainloop()
