from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(500, 400)
colours = ["red", "orange", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput("Make your bet", "Which turtle will win the race? Choose a colour: ").lower()
print(user_bet)

turtles = []

def turtle_start():
    y_axis = 150
    modifier = 0
    for i in range(0, 6):
        new_turtle = Turtle()
        new_turtle.shape("turtle")
        new_turtle.color(colours[i])
        new_turtle.penup()
        turtles.append(new_turtle)
        turtles[i].goto(-230, y_axis-modifier)
        modifier += 60

def turtle_race():
    for i in range(0, 6):
        while turtles[i].xcor() < 230:
            for i in range(0, 6):
                turtles[i].forward(random.randint(0, 10))
                if turtles[i].xcor() >= 230:
                    winner = colours[i]
                    return winner

turtle_start()
race_winner = turtle_race()
if user_bet == race_winner:
    print(f"Your choice, {user_bet}, won the race!")
else:
    print(f"You lose, {race_winner} has won")


screen.exitonclick()