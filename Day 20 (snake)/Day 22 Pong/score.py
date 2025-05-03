from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)

    def show_score(self, left_score, right_score):
        self.clear()
        self.write(f"{left_score} : {right_score}",align="center", font=("Arial", 20, "normal"))