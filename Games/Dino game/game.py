import turtle


class Dino(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("pink")
        self.penup()
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.left(90)


    def jump(self):
        self.forward(10)

    def down(self):
        self.backward(10)

import random


class Obstacle():
    def __init__(self):
        self.colors = ["red", "light green", "light blue", "yellow", "purple"]
        self.shapes = ["square", "triangle", "circle"]
        self.obstacles = []


    def make_obstacles(self):
        if random.randint(1,40) ==1:
            for i in range(0, 5):
                obstacle = turtle.Turtle()
                obstacle.shape(random.choice(self.shapes))
                obstacle.color(random.choice(self.colors))
                obstacle.penup()
                obstacle.shapesize(stretch_wid=random.randint(0,2)*0.4+0.2, stretch_len=random.randint(0,2)*0.5+0.2)
                obstacle.goto(500, random.randint(-500, 500))
                self.obstacles.append(obstacle)

        return 
    
    def move_obstacles(self,speed):
        for obstacle in self.obstacles:
            obstacle.backward(speed)
        return 
    
    def detect_collision(self,ddd,distance):
        for obstacle in self.obstacles:
            if abs(obstacle.xcor() - ddd.xcor() ) < distance and abs(obstacle.ycor() - ddd.ycor()) < distance:
                return 'break'
        return 'continue'
    
