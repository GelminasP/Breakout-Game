from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from blocks import Blocks
from scoreboard import Scoreboard, GameMessages
import time

screen = Screen()
game_messages = GameMessages()


def game():

    screen.bgcolor("black")
    screen.title("Breakout")
    screen.setup(width=800, height=600)
    screen.tracer(0)

    block_list = []
    paddle = Paddle()
    ball = Ball(block_list)
    scoreboard = Scoreboard()

    # Block setup
    x_list = [-340, -230, -120, -10, 100, 210, 320]
    y_list = [280, 255, 230, 205, 180]

    for i in x_list:
        for j in y_list:
            block = Blocks(i, j)
            block_list.append(block)

    # Physical Control Key Setup

    screen.listen()
    screen.onkey(paddle.move_left, "Left")
    screen.onkey(paddle.move_right, "Right")

    game_is_on = True

    while game_is_on:
        time.sleep(ball.move_speed)
        screen.update()
        ball.move()

        # Detect collision with the wall
        if ball.ycor() > 280:
            ball.bounce_y()

        if ball.xcor() > 380 or ball.xcor() < -380:
            ball.bounce_x()

        # Detect collision with a paddle
        if ball.distance(paddle) < 30 and ball.ycor() >= -250:
            ball.bounce_y()
        elif ball.ycor() < -250:
            game_is_on = False
            game_messages.gameover_message()
            game_messages.restart_info()

        # Detect collision with a block
        for i in block_list:
            if (i.ycor() - 20 <= ball.ycor() <= i.ycor() + 20) and (
                    i.xcor() - 60 < ball.xcor() < i.xcor() + 60) and ball.y_move > 0:
                i.goto(1000, 1000)
                ball.y_move *= -1
                block_list.remove(i)
                scoreboard.point()

        # Win condition
        if block_list == []:
            game_is_on = False
            game_messages.win_message()

# Start the game


def start_game():
    game()


# Restart the game


def restart_game():
    screen.clear()
    start_game()


start_game()
screen.onkey(restart_game, "r")


screen.exitonclick()
