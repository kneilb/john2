from tkinter import *
import random

# global constants
CANVAS_HEIGHT = 500
CANVAS_WIDTH = 500
PLAYER_SIZE = 30

CAR_MOVE_INTERVAL = 25

# global variables
car_speed = 0

# functions
def car_event(event):
    global car_speed
    print(event)
    k = event.keysym
    if k == "Up":
        # canvas.move(orb,-10,0)
        car_speed += 1
    elif k == "Down":
        # canvas.move(orb,10,0)
        car_speed -= 1

    print(f"Speed is {car_speed}")
def move_car():
    global car_speed
    pos = canvas.coords(car)
    # print(f"{pos[0]} {car_speed}")
    # Crash!
    if (pos[0] + car_speed) <= 0:
        print("crash!")
        car_speed = 0
    if (pos[0] + car_speed) >= CANVAS_WIDTH - PLAYER_SIZE:
        print("crash!")
        car_speed = 0
    
    canvas.move(car, car_speed, 0)

    window.after(CAR_MOVE_INTERVAL, move_car)

##########
## MAIN ##
##########
window = Tk()
window.title("car")

canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="blue")
canvas.pack()

car = canvas.create_oval(CANVAS_WIDTH/2 - PLAYER_SIZE/2, CANVAS_HEIGHT - PLAYER_SIZE, CANVAS_WIDTH/2 + PLAYER_SIZE/2, CANVAS_HEIGHT, fill="grey")

canvas.bind_all("<Key>", car_event)

window.after(CAR_MOVE_INTERVAL, move_car)
window.mainloop()
