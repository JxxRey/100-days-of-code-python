from turtle import Turtle
score_num = 0

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 260)
        self.color("white")
        self.penup()
        self.vis_scoreboard()


    def vis_scoreboard(self):
        self.write(("Score: " + str(score_num)), False, "center", ("Arial", 20, "normal"))
        self.hideturtle()

    def score_increase(self):
        global score_num
        score_num += 1
        self.clear()
        self.vis_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align= "center", font=("Arial", 20, "normal"))