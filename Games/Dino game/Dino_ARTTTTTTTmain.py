import turtle
from game import Dino, Obstacle


dino = Dino()
turtle.listen()
turtle.onkey(dino.jump, "space")

obs = Obstacle()
turtle.tracer(0, 0)
while True:

    obs.make_obstacles()
    obs.move_obstacles()

    turtle.Screen().update()




turtle.mainloop()