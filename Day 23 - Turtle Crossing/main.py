import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
car_manager = CarManager()
scoreboard = Scoreboard()
highscore = Scoreboard()
player = Player()

screen.listen()
screen.onkeypress(player.go_up, "Up")

game_is_on = True
score = 0
with open("highscore.txt") as file:
    saved_score = int(file.read())

while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move_car()

    if player.distance(0, 300) < 20:
        score +=1
        player.return_to_start()
        car_manager.speed_increase()
    for car in car_manager.car_list:
        if car.distance(player) < 25:
            game_is_on = False

    scoreboard.update_score(score)
    highscore.all_time_score(saved_score)
if score > saved_score:
    with open("highscore.txt", mode="w") as file:
        file.write(str(score))