import turtle
import random
from racingTurtle import Racing_turtle
import time


#screen size 
turtle.setup(500, 500)
# screen trace
turtle.tracer(0)

Racing_ttl = Racing_turtle()

turtles = Racing_ttl.make_turtles()

while True:
    for t in turtles:
        t.forward(random.randint(1, 50))
        if t.xcor() > 500:
            if t.pencolor() == "blue":
                print("umair wins")
                turtle.bgcolor("blue")
                turtle.write("umair wins", align="center", font=("Arial", 30, "normal"))
            elif t.pencolor() == "purple":
                print("andy wins")
                turtle.bgcolor("purple")
                turtle.write("andy wins", align="center", font=("Arial", 30, "normal"))
            else:
                print('angela wins')
                turtle.bgcolor("pink")
                turtle.write("angela wins", align="center", font=("Arial", 30, "normal"))   

            turtle.done()
        
    time.sleep(0.5)
    turtle.Screen().update()
    #get positon

    




turtle.mainloop()
