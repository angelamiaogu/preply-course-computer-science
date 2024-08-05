
import turtle 

# Left paddle


class Paddle:
    def __init__(self, x, y):
        self.paddle = turtle.Turtle()
        self.paddle.speed(0)
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(x, y)
        self.paddle.shapesize(stretch_wid=6, stretch_len=1)

    def move_up(self):
        y = self.paddle.ycor()
        y += 20
        self.paddle.sety(y)

    def move_down(self):
        y = self.paddle.ycor()
        y -= 20
        self.paddle.sety(y)



class Ball():
    def __init__(self, x, y,speed):
        self.ball = turtle.Turtle()
        self.ball.speed(0)
        self.ball.shape("circle")
        self.ball.color("white")
        self.ball.penup()
        self.ball.goto(x, y)
        self.speed = speed
        self.ball.dx = speed
        self.ball.dy = speed

    def move(self):
        self.ball.setx(self.ball.xcor() + self.ball.dx)
        self.ball.sety(self.ball.ycor() + self.ball.dy)

    def bounce_y(self):
        self.ball.dy *= -1

    def bounce_x(self):
        self.ball.dx *= -1

    def reset(self):
        self.ball.goto(0, 0)
        self.ball.dx = self.speed
        self.ball.dy = self.speed