import time
from food import Food
from turtle import Screen, Turtle
from snake import Snake
from  score import Score
screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("SNAKE")
screen.tracer(0)

score = Score()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")
game_on = True

while not score.game_over:
    screen.update()
    time.sleep(0.1)
    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh_food()
        snake.extend()
        score.update_score()
    elif snake.head.xcor() >= 300 or snake.head.xcor() <= -300:
        score.final_score()
    elif snake.head.ycor() >= 300 or snake.head.ycor() <= -300:
        score.final_score()
    for seg in snake.segments[1:]:
         if snake.head.distance(seg) < 10:
            score.final_score()


screen.exitonclick()