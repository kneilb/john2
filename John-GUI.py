from tkinter import *

window = Tk()
window.title("Chaos")

def orb_move(event):
    print(event)
    k = event.keysym
    if k == "Left":
        canvas.move(orb,-10,0)
    if k == "Right":
        canvas.move(orb,10,0)
    if k == "Up":
        canvas.move(orb,0,-10)
    if k == "Down":
        canvas.move(orb,0,10)

def words1():
    print("WELCOME TO CHAOSVILLE")
    display.config(text="WELCOME TO CHAOSVILLE", fg="red", bg="black")

button1=Button(window, text="DO NOT PRESS ME!!!", command=words1)
button1.pack()

display = Label(window, text="WELCOME TO NOWHERE")
display.pack()

canvas = Canvas(window, width=500,height=500)
canvas.pack()

orb = canvas.create_oval(100, 200, 130, 230, fill="red")


message = canvas.create_text(200, 200, text="WE ARE GOING MAD!?!", fill="black")

canvas.bind_all("<Key>", orb_move)
window.mainloop()
