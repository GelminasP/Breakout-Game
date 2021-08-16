from turtle import Turtle
import time


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(300, -300)
        self.write(self.score, align="center", font=("Courier", 30, "normal"))

    def point(self):
        self.score += 1
        self.update_scoreboard()


class GameMessages(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.penup()
        self.hideturtle()
        self.loss_message = "GAME OVER!"
        self.restart_message = "Press [R] to restart the game"
        self.win_message = "YOU WIN!"

    def gameover_message(self):
        self.goto(0, 0)
        self.write(self.loss_message, align="center", font=("Courier", 80, "normal"))
        time.sleep(2)
        self.clear()

    def restart_info(self):
        self.goto(0, -100)
        self.write(self.restart_message, align="center", font=("Courier", 20, "normal"))

    def win_message(self):
        self.goto(0, 0)
        self.write(self.win_message, align="center", font=("Courier", 20, "normal"))




