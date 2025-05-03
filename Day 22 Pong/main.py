import time
from turtle import Screen, Turtle
from paddle import Paddles
from ball import Ball
from score import Score
screen = Screen()
screen.bgcolor("black")
screen.setup(800, 600)
screen.title("Pong")
screen.listen()
screen.tracer(0)

###Creat paddles
left_paddle = Paddles((-350,0))
right_paddle = Paddles((350, 0))
ball = Ball()
score = Score()
###Move paddles
screen.onkeypress(left_paddle.go_up, "w")
screen.onkeypress(left_paddle.go_down, "s")
screen.onkeypress(right_paddle.go_up, "Up")
screen.onkeypress(right_paddle.go_down, "Down")


game_on = True
left_score = 0
right_score = 0

while game_on:
    score.show_score(left_score, right_score)
    screen.update()
    time.sleep(ball.speed_modifier)
    ball.ball_movement()
    ###Detect collision with paddles and change ball movement direction
    if ball.distance(left_paddle) < 50 and ball.xcor() < -350 or ball.distance(right_paddle) < 50 and ball.xcor() > 350:
        ball.paddle_bounce()

    ###Detect collision with sides and change ball movement direction
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    ###Detect if point is scored and reset ball
    if ball.xcor() >= 380:
        left_score += 1
        ball.restart()
    elif ball.xcor() <= -380:
        right_score += 1
        ball.restart()

screen.exitonclick()