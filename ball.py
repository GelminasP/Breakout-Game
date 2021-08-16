from turtle import Turtle


class Ball(Turtle):

    def __init__(self, block_list):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.goto(0, -200)
        self.x_move = 5
        self.y_move = 6
        self.move_speed = 0.02
        self.block_list = block_list

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1