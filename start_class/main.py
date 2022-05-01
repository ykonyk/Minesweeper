from calendar import c
from tkinter import *
from cell import Cell
import settings
import utiles


#instaciacion del objeto tkinter
root = Tk()

#sobreescribir ajustes del marco
root.configure(bg="black")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="black",
    width=settings.WIDTH,
    height=utiles.height_prct(25)
)
top_frame.place(x=0, y=0)

geme_title = Label(
    top_frame,
    bg="black",
    fg="white",
    text="Minesweeper game",
    font=("", 48)
)
geme_title.place(
    x = utiles.width_prct(25),
    y = 0
)

left_frame = Frame(
    root,
    bg="black",
    width=utiles.width_prct(25),
    height=utiles.height_prct(75)
)
left_frame.place(x=0, y=utiles.height_prct(25))

center_frame = Frame(
    root,
    bg="black",
    width=utiles.width_prct(75),
    height=utiles.height_prct(75)
)
center_frame.place(
    x=utiles.width_prct(25), 
    y=utiles.height_prct(25)
    )

for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c1 = Cell(x, y)
        c1.create_btn_object(center_frame)
        c1.cell_btn_object.grid(
            column=x,
            row=y
)
# LLamada label desde la clase Cell
Cell.create_cell_count_label(left_frame)
Cell.cell_count_label_object.place(x=0, y=0)
Cell.randomize_mines()

#ejecutar la ventana
root.mainloop()
