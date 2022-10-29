from tkinter import *
from copy import copy

import random

# global constants
CANVAS_HEIGHT = 480
CANVAS_WIDTH = 480
CELL_SIZE = 30
CELLS_X = int(CANVAS_WIDTH / CELL_SIZE)
CELLS_Y = int(CANVAS_HEIGHT / CELL_SIZE)

SNAKE_MOVE_INTERVAL = 500

# global variables
snake_velocity = (0,0)

snake_body = []
snake_colours = ["green", "red", "yellow"]
sweets = set()


# functions
def out_of_bounds(pos):
    return pos[0] < 0 or \
       pos[1] < 0 or \
       pos[0] > CELLS_X or \
       pos[1] > CELLS_Y

def to_canvas_x(x):
    return CELL_SIZE * x

def to_canvas_y(y):
    return CELL_SIZE * y

def spawn_sweet():
    sweet_pos = (
        random.randint(0, CELLS_X),
        random.randint(0, CELLS_Y)
    )

    if sweet_pos not in sweets:
        sweets.add(sweet_pos)

def sweet_present(x, y):
    sweet_pos = (x, y)
    return sweet_pos in sweets

def remove_sweet(x, y):
    sweet_pos = (x, y)
    sweets.remove(sweet_pos)

def add_new_segment(x, y, colour="green"):
    global snake_body

    snake_body.insert(0, [x, y])

def remove_last_segment():
    del snake_body[-1]

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
    global snake_velocity
    k = event.keysym

    if k == "Up":
        snake_velocity = (0, -1)
    elif k == "Down":
        snake_velocity = (0, 1)
    elif k == "Right":
        snake_velocity = (1, 0)
    elif k == "Left":
        snake_velocity = (-1, 0)

    print(f"Velocity is {snake_velocity}")

def move_snake():
    dead = False
    head_pos = snake_body[0]

    new_pos = copy(head_pos)
    new_pos[0] += snake_velocity[0]
    new_pos[1] += snake_velocity[1]

    print(head_pos, snake_velocity, "->", new_pos)

    if out_of_bounds(new_pos) or (snake_velocity != (0, 0) and new_pos in snake_body):
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

    for i, c in enumerate(snake_body):
        colour = snake_colours[i % len(snake_colours)]
        draw_segment(c[0], c[1], colour)

    for s in sweets:
        draw_sweet(s[0], s[1])

    if not dead:
        window.after(SNAKE_MOVE_INTERVAL, move_snake)

##########
## MAIN ##
##########
window = Tk()
window.title("snake!")

canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

add_new_segment(0, 0)
spawn_sweet()

canvas.bind_all("<Key>", key_event)

window.after(SNAKE_MOVE_INTERVAL, move_snake)
window.mainloop()
