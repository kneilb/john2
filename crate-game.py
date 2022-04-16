from tkinter import *
import random

window = Tk()
window.title("crate collecter")

CANVAS_HEIGHT = 500
CANVAS_WIDTH = 500
PLAYER_SIZE = 30
CRATE_SIZE = 30

canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

crate_type_list = ["red", "black"]

black_crates = []
red_crates = []

# functions
def orb_move(event):
    print(event)
    k = event.keysym
    if k == "Left":
        canvas.move(orb,-10,0)
    if k == "Right":
        canvas.move(orb,10,0)

def drop_crate():
    x_drop = random.randint(1, 470)
    y_drop = 0
    crate_type = random.choice(crate_type_list)
    crate = canvas.create_rectangle(x_drop, y_drop, x_drop + CRATE_SIZE, y_drop + CRATE_SIZE, fill=crate_type)
    if crate_type == "red":
        red_crates.append(crate)
    else:
        black_crates.append(crate)
    window.after(1000, drop_crate)

def move_crate():
    all_crates = black_crates + red_crates
    for c in all_crates:
        canvas.move(c, 0, crate_speed)
        if canvas.coords(c)[1] > CANVAS_HEIGHT:
            new_x = random.randint(1, 470)
            canvas.coords(c, new_x, 0, new_x + CRATE_SIZE, CRATE_SIZE)
    window.after(50, move_crate)

def collision(player, crate):
    x_close = abs(canvas.coords(player)[0] - canvas.coords(crate)[0])
    y_close = abs(canvas.coords(crate)[0] - canvas.coords(player)[0])

##########
## MAIN ##
##########
main_message = canvas.create_text(200, 200, text = "crate collecter!!!")
crates_got = 0
message1 = canvas.create_text(200, 300, text = f"you collected {crates_got} crates!")

orb = canvas.create_oval(CANVAS_WIDTH/2 - PLAYER_SIZE/2, CANVAS_HEIGHT - PLAYER_SIZE, CANVAS_WIDTH/2 + PLAYER_SIZE/2, CANVAS_HEIGHT, fill="blue")
canvas.bind_all("<Key>", orb_move)

crate_speed = 2

window.after(5000, drop_crate)
window.after(1000, move_crate)
window.mainloop()
