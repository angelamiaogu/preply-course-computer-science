import tkinter as tk
import random

global color

def change_color():
    global color
    color = "green" if color == "red" else "red"
    canvas.config(bg=color)
    if color == "green":
        canvas.bind("<Button-1>", on_click)
    else:
        canvas.unbind("<Button-1>")
    root.after(random.randint(1000, 5000), change_color)

color = 'red'
points = 0

def on_click(event):
    global points
    if color == 'green':
        points += 1
    else:
        points -= 3
    point_label.config(text=f'Points: {points}')

root = tk.Tk()
root.geometry('400x400')

point_label = tk.Label(root, text=f'Points: {points}')
point_label.pack()

canvas = tk.Canvas(root, width=400, height=400)
canvas.pack()

root.after(random.randint(1000, 5000), change_color)

root.mainloop()
