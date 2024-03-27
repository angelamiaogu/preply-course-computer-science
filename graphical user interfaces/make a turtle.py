import turtle 
import random
colors = ["pink", "red", "black", "blue", "green"]
angles = [0,90,180,270]
turtle.pensize(5)
turtle.colormode(255)
for i in range (1000):
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    turtle.color( (r,g,b) )
    turtle.forward(10)
    turtle.left(random.choice(angles))



turtle.mainloop()