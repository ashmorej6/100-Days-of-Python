from turtle import Turtle
FONT = ("Courier", 24, "normal")

#Scoreboard class, creates invisible turtle to write the score at the top of the screen.
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 260)

    def update_score(self, score):
        self.clear()
        self.write(f"Score: {score}", move=False, align="center", font=("Arial", 16, "normal"))

    def all_time_score(self,highscore):
        self.goto(0, 240)
        self.write(f"All time highscore: {highscore}", move=False, align="center", font=("Arial", 14, "normal"))