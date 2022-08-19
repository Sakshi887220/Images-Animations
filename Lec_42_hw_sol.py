from tkinter import *
import random


root= Tk()
root.title("Moving objects")
root.geometry("400x400")

width, height = 200, 200

canvas = Canvas(root,width= width,height= height, bg='white')
canvas.pack(pady=20)


"""img=PhotoImage(file="snake.png")
img=img.subsample(5)
shape=canvas.create_image(100,100,image=img)
"""

shape= canvas.create_oval(100,100,100+10,100+10,fill="yellow")
colors=["blue","yellow","black","orange","pink"]

def pressed(event):
    index=random.randrange(0,5)
    x,y=0,0
    if event.char == "a":
        x,y =-10,0
    if event.char == "d":
        x,y =10,0
    if event.char == "w":
        x,y =0,-10
    if event.char == "s":
        x,y =-0,10
    canvas.itemconfig(shape,fill=colors[index])
    canvas.move(shape,x,y)

root.bind("<Key>",pressed)

root.mainloop()

