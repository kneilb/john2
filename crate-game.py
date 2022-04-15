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

crate_type_list = ["red", "brown"]

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

# main
main_message = canvas.create_text(200, 200, text = "crate collecter!!!")
crates_got = 0
message1 = canvas.create_text(200, 300, text = f"you collected {crates_got} crates!")

orb = canvas.create_oval(CANVAS_WIDTH/2 - PLAYER_SIZE/2, CANVAS_HEIGHT - PLAYER_SIZE, CANVAS_WIDTH/2 + PLAYER_SIZE/2, CANVAS_HEIGHT, fill="blue")
canvas.bind_all("<Key>", orb_move)

brown_crate = 0
red_crate = 0
crate_supply_speed = 2
drop_crate()
window.after(50, drop_crate)
window.mainloop()
