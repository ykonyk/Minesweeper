from tkinter import Button
import random
import settings

class Cell:

    all = []

    # metodo constructor que se ejecutara nada mas instanciarse la clase
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y
        # añadir todas las instancias de objetos boton a la lista-> all
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            bg="pink"
        )
        btn.bind("<Button-1>", self.left_click_actions)
        btn.bind("<Button-3>", self.right_click_actions)
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()
        else:
            self.show_cell()
    
    # devuelve un objeto basado en el valor de x, y
    def get_cell_by_axis(self, x, y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell
    
    def show_cell(self):
        print(self.get_cell_by_axis(0, 0))
    
    def show_mine(self):
        self.cell_btn_object.configure(bg="red")

    def right_click_actions(self, event):
        print(event)
        print("Derecha")

    # metodo estatico pertece a la clase global y no cada instancia
    @staticmethod
    def randomize_mines(): 
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
            picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"