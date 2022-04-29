from tkinter import *
import settings
import utiles

#instaciacion del objeto tkinter
root = Tk()

#sobreescribir ajustes del marco
root.configure(bg="purple")
root.geometry(f"{settings.WIDTH}x{settings.HEIGHT}")
root.title("Minesweeper game")
root.resizable(False, False)

top_frame = Frame(
    root,
    bg="blue",
    width=settings.WIDTH,
    height=utiles.height_prct(25)
)
top_frame.place(x=0, y=0)

left_frame = Frame(
    root,
    bg="yellow",
    width=utiles.width_prct(25),
    height=utiles.height_prct(75)
)
left_frame.place(x=0, y=utiles.height_prct(25))

center_frame = Frame(
    root,
    bg="pink",
    width=utiles.width_prct(75),
    height=utiles.height_prct(75)
)
center_frame.place(
    x=utiles.width_prct(25), 
    y=utiles.height_prct(25)
    )

#ejecutar la ventana
root.mainloop()
