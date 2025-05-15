from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

#Car creation class, includes creation of multiple cars within list,
#random colour choice, random y posision as well as movement across screen and speed increase.
class CarManager:
    def __init__(self):
        self.car_list= []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_number = random.randint(1, 6)
        if random_number == 1:
            random_y = random.randint(-260, 260)
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1,stretch_len=2)
            new_car.penup()
            new_car.goto(260, random_y)
            new_car.color(random.choice(COLORS))
            self.car_list.append(new_car)

    def move_car(self):
        for car in self.car_list:
            car.backward(self.car_speed)

    def speed_increase(self):
        self.car_speed += MOVE_INCREMENT
