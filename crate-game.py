from tkinter import *
import random

CANVAS_HEIGHT = 500
CANVAS_WIDTH = 500
PLAYER_SIZE = 30
CRATE_SIZE = 30

death_phrase = ["OW!!! That was a big hedgehog!",
"BANG!!! Ow... That was T.N.T",
"A cheesemonkey!!! Nooooooooooooooo...",
"NO!!! BAD DORIS!!! ARGHHHHHHH, MY ARM!!!",
"Wot? A house? SPLAT... OW.",
"KILLER SUDOKU!!! IT WILL KILL ME!!!",
"YOU WIN... DEATH!!!",
"To be honest, you did quite well.",
"JOHN IS BETTER THAN YOU!!!",
"JOHN IS BETTER THAN YOU!!!",
"JOHN IS BETTER THAN YOU!!!",
"JOHN IS BETTER THAN YOU!!!",
"JOHN IS BETTER THAN YOU!!!",
"<there was an error>, <you are MEH>",
"DID Y0U uNdErStAnD tH4T yOuR SC0RE WAS O? N0? N0? WeLl IT W4S... L00K... HA HA just kidding (;"]

# functions
def orb_move(event):
    # print(event)
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
    if playing:
        window.after(1000, drop_crate)

def move_crate():
    all_crates = black_crates + red_crates
    for c in all_crates:
        canvas.move(c, 0, crate_speed)
        if canvas.coords(c)[1] > CANVAS_HEIGHT:
            new_x = random.randint(1, 470)
            canvas.coords(c, new_x, 0, new_x + CRATE_SIZE, CRATE_SIZE)
    if playing:
        window.after(50, move_crate)

def collision(item1, item2, distance):
    item1_coords = canvas.coords(item1)
    item2_coords = canvas.coords(item2)
    x_diff = abs(item1_coords[0] - item2_coords[0])
    y_diff = abs(item1_coords[1] - item2_coords[1])
    return x_diff < distance and y_diff < distance

def check_collisions():
    for c in red_crates:
        hit = collision(orb, c, CRATE_SIZE)
        if hit:
            death()
    for c in black_crates:
        hit = collision(orb, c, CRATE_SIZE)
        if hit:
            update_score()
            canvas.delete(c)
            black_crates.remove(c)
    window.after(50, check_collisions)

def update_score():
    global crates_got
    global crate_speed
    global message1
    crates_got += 1
    message1.config(text = f"you collected {crates_got} crates!")
    if crates_got % 2 == 1:
        crate_speed += 1

def death():
    global playing
    if playing:
        game_over = canvas.create_text(150, 150, text=random.choice(death_phrase))
        playing = False

##########
## MAIN ##
##########
window = Tk()
window.title("crate collecter")

canvas = Canvas(window, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
canvas.pack()

crate_type_list = ["red"]
for i in range(5):
    crate_type_list.append("black")

black_crates = []
red_crates = []

playing = True
main_message = canvas.create_text(200, 200, text="crate collecter!!!")
# main_message.config()
crates_got = 0
message1 = Label(window, text=f"you collected {crates_got} crates!")
message1.pack()

orb = canvas.create_oval(CANVAS_WIDTH/2 - PLAYER_SIZE/2, CANVAS_HEIGHT - PLAYER_SIZE, CANVAS_WIDTH/2 + PLAYER_SIZE/2, CANVAS_HEIGHT, fill="blue")

canvas.bind_all("<Key>", orb_move)

crate_speed = 2

window.after(5000, drop_crate)
window.after(1000, move_crate)
window.after(1500, check_collisions)
window.mainloop()
