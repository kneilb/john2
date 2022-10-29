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
        car_speed += 0.25
    elif k == "Down":
        # canvas.move(orb,10,0)
        car_speed -= 0.25

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

def turbo_button():
    car_speed + 1

##########
## MAIN ##
##########
window = Tk()
window.title("VACS")

button1 = Button(window, text="Turbo", fg="white", bg="black", command=turbo_button)
button1.pack()

display1 = Label(window, text="VERY ACCURATE CAR SIMULATOR")
display1.pack()

canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="blue")
canvas.pack()

body = canvas.create_rectangle(
    CANVAS_WIDTH/2 - PLAYER_SIZE/2 - PLAYER_SIZE,
    CANVAS_HEIGHT - PLAYER_SIZE - PLAYER_SIZE/2,
    CANVAS_WIDTH/2 + PLAYER_SIZE/2 + PLAYER_SIZE*4,
    CANVAS_HEIGHT - PLAYER_SIZE/2, 
    fill="red"
)
car = canvas.create_oval(
    CANVAS_WIDTH/2 - PLAYER_SIZE/2,
    CANVAS_HEIGHT - PLAYER_SIZE,
    CANVAS_WIDTH/2 + PLAYER_SIZE/2,
    CANVAS_HEIGHT, 
    fill="black")
wheel2 = canvas.create_oval(
    CANVAS_WIDTH/2 - PLAYER_SIZE/2 + 3 * PLAYER_SIZE,
    CANVAS_HEIGHT - PLAYER_SIZE,
    CANVAS_WIDTH/2 + PLAYER_SIZE/2 + 3 * PLAYER_SIZE, 
    CANVAS_HEIGHT,
    fill="black")

canvas.bind_all("<Key>", car_event)

window.after(CAR_MOVE_INTERVAL, move_car)
window.mainloop()
