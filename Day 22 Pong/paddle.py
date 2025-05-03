from turtle import Turtle

class Paddles(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(coordinates)

    def create_paddle(self, coord):
        self.paddle = Turtle("square")
        self.paddle.color("white")
        self.paddle.shapesize(5, 1)
        self.paddle.penup()
        self.paddle.goto(coord)

    ###Move Paddles
    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

