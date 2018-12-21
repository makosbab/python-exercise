import math
from tkinter import *

COLORS  =[
    'gray1', 'gray2', 'gray3', 'gray4', 'gray5', 'gray6', 'gray7', 'gray8', 'gray9', 'gray10',
    'gray11', 'gray12', 'gray13', 'gray14', 'gray15', 'gray16', 'gray17', 'gray18', 'gray19',
    'gray20', 'gray21', 'gray22', 'gray23', 'gray24', 'gray25', 'gray26', 'gray27', 'gray28',
    'gray29', 'gray30', 'gray31', 'gray32', 'gray33', 'gray34', 'gray35', 'gray36', 'gray37',
    'gray38', 'gray39', 'gray40', 'gray42', 'gray43', 'gray44', 'gray45', 'gray46', 'gray47',
    'gray48', 'gray49', 'gray50', 'gray51', 'gray52', 'gray53', 'gray54', 'gray55', 'gray56',
    'gray57', 'gray58', 'gray59', 'gray60', 'gray61', 'gray62', 'gray63', 'gray64', 'gray65',
    'gray66', 'gray67', 'gray68', 'gray69', 'gray70', 'gray71', 'gray72', 'gray73', 'gray74',
    'gray75', 'gray76', 'gray77', 'gray78', 'gray79', 'gray80', 'gray81', 'gray82', 'gray83',
    'gray84', 'gray85', 'gray86', 'gray87', 'gray88', 'gray89', 'gray90', 'gray91', 'gray92',
    'gray93', 'gray94', 'gray95', 'gray97', 'gray98', 'gray99']

angle = 137.5
c = 5
n = 0
DOT_RADIUS = 2
WIDTH = 600
HEIGHT = 600


def animate(n):
    # global n
    # theta = n * angle
    theta = n * math.radians(angle)
    r = c* math.sqrt(n)
    x = r * math.cos(theta)
    y = r * math.sin(theta)
    color = "#000000"
    canvas.create_oval(WIDTH/2 + x-DOT_RADIUS, 
            HEIGHT/2 + y-DOT_RADIUS, 
            WIDTH/2 + x+DOT_RADIUS, 
            HEIGHT/2 + y+DOT_RADIUS,
            fill=COLORS[int(theta) % len(COLORS)],
            outline="")
    print((x ,y))
    n += 1
    if abs(x) < WIDTH / 2:
        root.after(3, animate, n)

root = Tk()
canvas = Canvas(root, width=WIDTH, height=HEIGHT, bg = "black")
canvas.pack()
animate(n)
root.mainloop()