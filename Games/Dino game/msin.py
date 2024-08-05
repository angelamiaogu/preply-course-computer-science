import turtle
from game import Dino, Obstacle

# Initialize the Dino and Obstacle objects
dino = Dino()
obs = Obstacle()

# Flags to track key states
up_pressed = False
down_pressed = False

# Function to start moving the dino up
def start_move_up():
    global up_pressed
    up_pressed = True

# Function to stop moving the dino up
def stop_move_up():
    global up_pressed
    up_pressed = False

# Function to start moving the dino down
def start_move_down():
    global down_pressed
    down_pressed = True

# Function to stop moving the dino down
def stop_move_down():
    global down_pressed
    down_pressed = False

# Set up the key press and release events
turtle.listen()
turtle.onkeypress(start_move_up, "Up")
turtle.onkeyrelease(stop_move_up, "Up")
turtle.onkeypress(start_move_down, "Down")
turtle.onkeyrelease(stop_move_down, "Down")

# Set up the game loop
turtle.tracer(0, 0)
speed = 5

scores = 0
while True:
    #update score

    scores += 1
    if scores % 1000 == 0:
        speed += 1

    if up_pressed:
        dino.jump()
    if down_pressed:
        dino.down()
        
    obs.make_obstacles()
    obs.move_obstacles(speed=speed)
    turtle.Screen().update()

    ans = obs.detect_collision(dino, distance=20)
    if ans == 'break':
        turtle.Write("Game Over", align="center", font=("Arial", 50, "normal"))
        break

turtle.mainloop()
