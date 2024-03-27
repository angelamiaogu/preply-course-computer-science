import turtle

# Create a turtle screen and set background color
screen = turtle.Screen()
screen.bgcolor("white")

# Create a turtle
circle_turtle = turtle.Turtle()
circle_turtle.shape("turtle")
circle_turtle.color("blue")
circle_turtle.speed(2)

# Draw a circle
circle_turtle.circle(100)

# Keep the window open until closed by the user
turtle.mainloop()
