import tkinter as tk

CANVAS_WIDTH, CANVAS_HEIGHT = 600, 400

root = tk.Tk()

canvas = tk.Canvas(root, width = CANVAS_WIDTH, height = CANVAS_HEIGHT)

# Début de votre code


x = CANVAS_WIDTH/2
y1 = 50
y2 = CANVAS_HEIGHT -50

canvas.create_line(x, y1, x, y2)

canvas.create_oval(x-50,y1+50,x+50,y1-50)
canvas.create_oval(x-50, y2+50, x+50, y2-50)
canvas.create_oval(x-50, (CANVAS_HEIGHT/2)+50,x+50,(CANVAS_HEIGHT/2)-50)

canvas.grid(column=0,row=0)
root.mainloop()
