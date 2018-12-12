import numpy
import random
from tkinter import *
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
RESOLUTION = 100
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

    def become_alive(self):
        self.state = 1

    def count_nbs(self, generation):
        # let col = (x + i + cols) % cols;
        # let row = (y + j + rows) % rows;
        # top_row = generation[(self.offset - (COLUMNS + 1)) % COLUMNS : (self.offset - (COLUMNS - 2)) % COLUMNS]
        # same_row = [generation[(self.offset -1)  % COLUMNS], generation[(self.offset + 1) % COLUMNS]]
        # bottom_row = generation[self.offset + (COLUMNS - 1) : self.offset + (COLUMNS + 2) % COLUMNS]
        # for t in top_row + same_row + bottom_row:
        #     print(t)
        #     if t.state == 1:
        #         self.nbs +=1
        # if generation[self.offset + 1].state == 1:
        #     print("YESH")
        north = generation[get_offset(3,2)]
        south = generation[(self.col + ROWS) % (ROWS * COLUMNS)]
        # i + 1 - ((i mod 8) div 7) * 8
        west = generation[(self.offset - 1 + (ROWS * COLUMNS)) % (ROWS * COLUMNS)]
        east = generation[(self.offset + COLUMNS +1) % (ROWS * COLUMNS)]
        print(north)

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
for i in first_generation:
    print((i.row, i.col, i.state))

c1 = first_generation[5]
print("Selected cell: {}".format(c1))
c1.count_nbs(first_generation)

root = Tk()
canvas = Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()
for i in first_generation:
    x_0 = i.col  * RESOLUTION
    y_0 = i.row  * RESOLUTION
    x_1 = (i.col + 1)  * RESOLUTION
    y_1 = (i.row + 1)  * RESOLUTION


    if i.state == 1:
        canvas.create_rectangle(x_0, y_0, x_1, y_1, fill="grey")

root.mainloop()
