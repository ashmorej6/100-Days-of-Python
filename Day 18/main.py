import turtle
import random
from turtle import Turtle

colour_list = (234, 232, 227), (230, 233, 239), (239, 231, 235), (228, 235, 231), (199, 162, 100), (62, 91, 128)

def random_color():
    r = random.random()
    g = random.random()
    b = random.random()
    colour = (r, g, b)
    return colour

### Random_direction function unused in final iteration
### Was created for use earlier in the project
def random_direction():
    direction = random.randint(0, 360)
    timmy.seth(direction)
    timmy.forward(25)

### Draw_circle function also unused, earlier challenge was a spirograph.
def draw_circle(gap):
    for _ in range(int(360 / gap)):
        random_color()
        timmy.circle(100)
        timmy.seth(timmy.heading() + gap)

def draw_dot_line():
    for _ in range(12):
        timmy.dot(10, random.choice(colour_list))
        timmy.forward(50)

def return_next_line():
    timmy.dot(10, random.choice(colour_list))
    timmy.right(90)
    timmy.forward(50)
    timmy.right(90)
    timmy.forward(600)
    timmy.right(180)

turtle.colormode(255)
turtle.screensize(500, 500)
timmy = Turtle()
timmy.shape("turtle")
timmy.speed("fastest")
timmy.penup()
timmy.goto(-300, 300)
for i in range(12):
    draw_dot_line()
    return_next_line()



screen = turtle.Screen()
screen.exitonclick()
