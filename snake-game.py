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
snake_colours = []
sweets = []


# functions
def to_canvas_x(x):
    return CELL_SIZE * x

def to_canvas_y(y):
    return CELL_SIZE * y

def to_cell_x(x):
    return x / CELL_SIZE

def to_cell_y(y):
    return y / CELL_SIZE


def spawn_sweet():
    sweet_pos = (
        random.randint(0, CELLS_X),
        random.randint(0, CELLS_Y)
    )

    if sweet_pos not in sweets:
        sweets.append(sweet_pos)


def add_new_segment(x, y, colour="green"):
    global snake_body

    new_segment = canvas.create_oval(
        to_canvas_x(x),
        to_canvas_y(y),
        to_canvas_x(x + 1),
        to_canvas_y(y + 1),
        fill=colour
    )
    snake_body.insert(0, new_segment)


def eat_sweet(x, y):
    # in the position the last segment of the snake "moved from"
    last_segment = snake_body[-1]
    add_new_segment(last_segment, y)

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

    # print(event.keysym)
    print(f"Velocity is {snake_velocity}")

def sweet_present(*args):
    return False

def move_snake():
    pos = canvas.coords(snake_body[0])

    new_pos = copy(pos)
    new_pos[0] += snake_velocity[0] * CELL_SIZE
    new_pos[1] += snake_velocity[1] * CELL_SIZE
    new_pos[2] += snake_velocity[0] * CELL_SIZE
    new_pos[3] += snake_velocity[1] * CELL_SIZE

    print(pos, snake_velocity, "->", new_pos)

    if new_pos[0] < 0 or \
       new_pos[1] < 0 or \
       new_pos[2] > CANVAS_WIDTH or \
       new_pos[3] > CANVAS_HEIGHT:
        print("crash!")
        # TODO: dead
        # TODO: also dead if we hit a bit of our own body!
    elif sweet_present(new_pos):
        pass
    else:
        # canvas.coords(snake_body[0], new_pos[0], new_pos[1], new_pos[2], new_pos[3])
        add_new_segment(to_cell_x(new_pos[0]), to_cell_y(new_pos[1]))
        canvas.delete(snake_body[-1])

    #TODO!!
    sweet_on_new_space = True
    if sweet_on_new_space:
        # last_seg_coords = canvas.coords(snake_body[-1])
        # new_segment_position = to_cell_x(last_seg
        pass

    # Loop through and move them all
    # Add on the new one

    

    # TODO: if new position contains a sweet, add a new body piece at the last piece's position instead

    window.after(SNAKE_MOVE_INTERVAL, move_snake)

##########
## MAIN ##
##########
window = Tk()
window.title("car")

canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

add_new_segment(0, 0)

canvas.bind_all("<Key>", key_event)

window.after(SNAKE_MOVE_INTERVAL, move_snake)
window.mainloop()
