import turtle

class Racing_turtle():
    def __init__(self):
        self.turtles = []
        self.y_positions = [0, 300, -300]
        self.colors = ["pink", "purple", "blue"]
        


    def make_turtles(self):
        for i in range(0, 3):
            tt = turtle.Turtle()
            tt.shape("turtle")
            tt.color(self.colors[i])
            tt.penup()
            tt.goto(-200, self.y_positions[i])
            self.turtles.append(tt)
        return self.turtles

