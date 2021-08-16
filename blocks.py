from turtle import Turtle
import random


class Blocks(Turtle):

    def __init__(self, xpos, ypos):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.colors = ['red', 'blue', 'green', 'cyan', 'yellow', 'orange', 'purple']
        self.goto(xpos, ypos)
        self.color(random.choice(self.colors))
        self.speed("fastest")

