import tkinter as tk
from PIL import Image, ImageTk
import random

master = tk.Tk()

master.title('BunnybunnYbuNny')
master.geometry("500x500")

canvas = tk.Canvas(master, bg='lightpink', width=500, height=500)
canvas.pack()

bunny_image = ImageTk.PhotoImage(Image.open("angelasbunny.png").resize((100, 100)))
bunny = canvas.create_image(50, 50, image=bunny_image)

carrot_image = ImageTk.PhotoImage(Image.open("carrot2.png").resize((50, 50)))
carrot = canvas.create_image(400, 400, image=carrot_image)

# Define a global variable to store the bunny object
global bunny_obj
bunny_obj = bunny

def jump(event):
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    canvas.move(bunny_obj, x, y)
    x,y = (canvas.coords(bunny))
    if x > 500 or y > 500:
        canvas.move(bunny_obj,-x,-y)#??????
    # tomorrow we have to stop rabit from going ouside screen
    a,b = (canvas.coords(carrot))
    d = ((x-a)**2 + (y-b)**2) ** 1/2
    print('distance',d)
    if a > 500 or b > 500:
        canvas.move(carrot,-a+100,-b+100)#??????
        
    if d <3000:
        print('closest distace achieved')
        print('carrot is in danger')
        a1 = random.randint(1,100)
        a2= random.randint(1,100)
        canvas.move(carrot,a1,a2)
        
        
        

canvas.bind("<Button-1>", jump)
master.mainloop()
