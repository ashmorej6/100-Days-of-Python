from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.game_over = False
        self.pencolor("white")
        self.hideturtle()
        self.penup()
        self.goto(-240, 260)
        self.write(f"Current score: {self.score}", align="center", font=("Arial", 12, "normal"))

    def update_score(self):
        self.clear()
        self.score += 1
        self.penup()
        self.goto(-240, 260)
        self.write(f"Current score: {self.score}", align= "center", font=("Arial", 12, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score

    def final_score(self):
        self.goto(0, 0)
        self.pensize(-60)
        self.write(f"Game over! Your final score is: {self.score}", align= "center", font=("Arial", 18, "normal"))
        self.game_over = True