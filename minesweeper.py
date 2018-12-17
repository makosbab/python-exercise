import random
from tkinter import *
WIDTH = 500 + 1 
HEIGHT = 500 + 1
RESOLUTION = 50
ROWS = HEIGHT // RESOLUTION
COLUMNS = WIDTH // RESOLUTION

def get_offset(row, col):
    return (row * COLUMNS) + col

def get_row(offset):
    return offset // ROWS

def get_col(offset):
    return offset % COLUMNS

class Cell(object):
    def __init__(self, bee=False, row = 0, col = 0):
        self.isBee = bee
        self.row = row
        self.col = col
        self.offset = get_offset(row, col)
        self.nbs = 0
        self.revealed = True


    def die(self):
        self.state = 0
        # print("Cell at ({}, {}) with {} neighbours has died!".format(self.row, self.col, self.nbs))

    def become_alive(self):
        self.state = 1
        # print("Cell at ({}, {}) with {} neighbours has come to life!".format(self.row, self.col, self.nbs))

    def count_nbs(self, generation):
        if self.isBee:
            return -1
        
        for i in range(-1, 2):
            for j in range(-1, 2):
                neighbour = generation[
                    get_offset(
                    (i+self.row + ROWS) % (ROWS),
                    (j+self.col + COLUMNS) % (COLUMNS)
                    )
                    ]
                if neighbour.offset == self.offset:
                    continue

                if neighbour.state == 1:
                    self.nbs += 1

    def __str__(self):
        return "Cell, index=({}, {}), offset={}, state={}".format(self.row, self.col, self.offset, self.state)

    

bees = list(
    Cell(
        random.choice((True, False)),
        get_row(i),
        get_col(i)
    ) for i in range(ROWS * COLUMNS)
)



def mouse_clicked(event):
    print(event.x, event. y)


root = Tk()
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.bind("<Button-1>", mouse_clicked)
canvas.pack()

def reveal():
    pass

def draw_canvas(canvas):


    for b in bees:
        print((b.isBee, b.col, b.row))

        x_0 = b.col  * RESOLUTION
        y_0 = b.row  * RESOLUTION
        x_1 = (b.col + 1)  * RESOLUTION
        y_1 = (b.row + 1)  * RESOLUTION

        if b.isBee:
            offset = 8
            canvas.create_rectangle(x_0, y_0, x_1, y_1, fill="grey", outline="")
            canvas.create_oval(x_0 + offset, y_0 + offset, x_1 - offset, y_1 - offset,
                fill="white",
                outline="black")
        else:
            canvas.create_rectangle(x_0, y_0, x_1, y_1, fill="white", outline="")

 
    for row in range(ROWS + 1):  
        canvas.create_line(0, (row) * RESOLUTION, COLUMNS * RESOLUTION, (row) * RESOLUTION)
    for col in range(COLUMNS + 1):
        canvas.create_line((col) * RESOLUTION, 0, (col) * RESOLUTION, ROWS * RESOLUTION)
draw_canvas(canvas)
root.mainloop()

