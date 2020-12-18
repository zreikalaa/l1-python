import tkinter as tk


def get_color(r=0, g=0, b=0):
    """ Retourne une couleur à partir de ses composantes r, g, b"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)

print(get_color(12,2,1))

"""racine = tk.Tk()
colors = ["blue",  "green", "black", "yellow", "magenta", "red"]
cote = 500
canvas = tk.Canvas(racine, width=cote, height=cote, bg="black")
canvas.grid()

nombre_cercle = 30
epaisseur = 500//(nombre_cercle*2)

for i in range(nombre_cercle):
    canvas.create_oval(epaisseur*i, epaisseur*i, cote-epaisseur*i, cote-epaisseur*i,
    fill=colors[i % len(colors)], outline=colors[i % len(colors)])

racine.mainloop()
"""