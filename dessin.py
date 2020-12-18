import tkinter as tk
import random
from functools import partial
root = tk.Tk()


def c_forme(forme):
    
    x1= random.randint(0, 500)
    y1= random.randint(0, 300)
    
    if forme == "cercle":
        canvas.create_oval(x1,y1 , x1+100, y1+100, fill = "blue") 
    
    if forme == "carré":
        canvas.create_rectangle((x1,y1) , (x1+100, y1+100), fill = "red")    
    
    if forme == "croix":
        canvas.create_rectangle((x1+40, y1),(x1+60, y1+100), fill="yellow")
        canvas.create_rectangle((x1, y1+40),(x1+100, y1+60), fill="yellow")    

canvas= tk.Canvas(root,width = 600, height = 400, bg="black")
canvas.grid(columnspan = 4, row = 0)


button1= tk.Button(root, text="cercle", fg = "blue", bg = "magenta", command=partial(c_forme,"cercle"))
button1.grid(column = 0, row = 1)

button2= tk.Button(root, text="carré", fg = "red", bg = "magenta", command=partial(c_forme,"carré"))
button2.grid(column = 1, row = 1)

button3= tk.Button(root, text="croix", fg = "yellow", bg="magenta", command=partial(c_forme,"croix"))
button3.grid(column = 2, row = 1)

root.mainloop()