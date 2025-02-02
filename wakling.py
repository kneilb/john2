from tkinter import *

window = Tk()
window.title("Wakling")

orb = None
colour = "black"

def orb_move(event):
    global colour
    print(event)

    # TODO: Needs Python 3.10
    # match event.keysym:
    #   case "Left":

    k = event.keysym
    if k == "Left":
        canvas.move(orb,-10,0)
    if k == "Right":
        canvas.move(orb,10,0)
    if k == "Up":
        canvas.move(orb,0,-10)
    if k == "Down":
        canvas.move(orb,0,10)
    if k == "space":
        x1, y1, x2, y2 = canvas.coords(orb)
        canvas.create_oval(x1, y1, x2, y2, fill=colour)
    if k == "BackSpace":
        x1, y1, x2, y2 = canvas.coords(orb)
        canvas.create_oval(x1, y1, x2, y2, fill="white", outline="white")
    if k == "1":
        colour = "black"
    if k == "2":
        colour = "blue"
    if k == "3":
        colour = "red"
    if k == "4":
        colour = "yellow"
    if k == "5":
        colour = "green"
    if k == "6":
        colour = "purple"
    if k == "7":
        colour = "pink"

def words1():
    global orb
    display.config(text="WELCOME TO WAKLING", fg="red", bg="black")
    orb = canvas.create_oval(100, 200, 130, 230, fill="blue")

button1=Button(window, text="PRESS TO PLAY", command=words1)
button1.pack()

display = Label(window, text="WAKLING GAME")
display.pack()

canvas = Canvas(window, width=500, height=500, bg="white")
canvas.pack()

message = canvas.create_text(200, 200, text="wH333! i lUv dIs!", fill="green", font = ("fish", 34))

canvas.bind_all("<Key>", orb_move)
window.mainloop()
