from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xdir = 10
        self.ydir = 10
        self.speed_modifier = 0.1

    def restart(self):
        self.goto(0,0)
        self.speed_modifier = 0.1
        self.coinflip = random.random()
        if self.coinflip < 0.5:
            self.paddle_bounce()

    def ball_movement(self):
        new_x = self.xcor() + self.xdir
        new_y= self.ycor() + self.ydir
        self.goto(new_x, new_y)

    def bounce(self):
        self.ydir *= -1

    def paddle_bounce(self):
        self.xdir *= -1
        self.speed_modifier *= 0.9
