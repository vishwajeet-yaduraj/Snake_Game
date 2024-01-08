from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 20, 'normal')


class Scorecard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(-0, 270)
        self.current_score = 0
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def update_score(self):
        self.write(f"My Score = {self.current_score}", False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.update_score()



