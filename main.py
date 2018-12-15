import numpy
import random
from tkinter import *
from time import sleep
def add_book_name(f):
    def wrapper():
        return f() + "fav book"
    return wrapper

@add_book_name
def read_book():
    return "Reading: "

print(read_book())
WIDTH = 500
HEIGHT = 500
RESOLUTION = 20
ROWS = HEIGHT // RESOLUTION
COLUMNS = WIDTH // RESOLUTION


class Cell(object):
    def __init__(self, state=0, row = 0, col = 0):
        self.state = state
        self.row = row
        self.col = col
        self.offset = get_offset(row, col)
        self.nbs = 0

    def die(self):
        self.state = 0
        # print("Cell at ({}, {}) with {} neighbours has died!".format(self.row, self.col, self.nbs))

    def become_alive(self):
        self.state = 1
        # print("Cell at ({}, {}) with {} neighbours has come to life!".format(self.row, self.col, self.nbs))

    def count_nbs(self, generation):
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

def get_offset(row, col):
    return (row * COLUMNS) + col

def get_row(offset):
    return offset // ROWS

def get_col(offset):
    return offset % COLUMNS



first_generation = list(
    Cell(
        random.randint(0, 1),
        get_row(i),
        get_col(i)
    ) for i in range(ROWS * COLUMNS)
)


# for c in first_generation:
#     c.count_nbs(first_generation)


def animate(old_generation):
    
    for i in old_generation:
        x_0 = i.col  * RESOLUTION
        y_0 = i.row  * RESOLUTION
        x_1 = (i.col + 1)  * RESOLUTION
        y_1 = (i.row + 1)  * RESOLUTION

        color_fill = "grey" if i.state == 1 else "white"
        canvas.create_rectangle(x_0, y_0, x_1, y_1, fill=color_fill, outline="")
        # print(i)
    # next_generation = move_to_next_generation(first_generation)
        next_generation = list()

    for old_cell in old_generation:
        old_cell.count_nbs(old_generation)
        new_cell = old_cell
        if old_cell.state == 0 and old_cell.nbs == 3:
            new_cell.become_alive()
        elif old_cell.state == 1 and (old_cell.nbs < 2 or old_cell.nbs > 3):
            new_cell.die()
        else:
            new_cell.state = old_cell.state
        next_generation.append(new_cell)
    root.after(2, animate, next_generation)

def move_to_next_generation(old_generation):
# print("Neighbours: {}".format(c1.nbs))
    next_generation = list()
    for old_cell in old_generation:
        old_cell.count_nbs(old_generation)
        new_cell = old_cell
        if old_cell.state == 0 and old_cell.nbs == 3:
            new_cell.become_alive()
        elif old_cell.state == 1 and (old_cell.nbs < 2 or old_cell.nbs > 3):
            new_cell.die()
        else:
            new_cell.state = old_cell.state
        next_generation.append(new_cell)
    return next_generation

root = Tk()
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
animate(first_generation)
root.mainloop()

# while True:
#     move_to_next_generation(first_generation)
