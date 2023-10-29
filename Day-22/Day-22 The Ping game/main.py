import random
from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("green")
screen.title("Welcome to the Ping Game!")
screen.tracer(0)

r_paddle = Paddle((350,  0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move_ball()

# Detect the collision wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
# Detect the collision with r_paddle
    if ball.distance(r_paddle) < 50 and ball.ycor() < 340 or ball.distance(l_paddle) < 50 and ball.ycor() < 340:
        ball.bounce_x()
# Detect the R paddle Misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_points()

# Detect the L paddle Misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_points()

screen.exitonclick()
