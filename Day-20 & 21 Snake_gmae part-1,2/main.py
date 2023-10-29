from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("light green")
screen.title("Welcome to Snake Game")
screen.tracer(0)

# create a new snake object from tne class

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    # Distance from snake.head to the food < pixel of the food within 15
    if snake.head.distance(food) < 15:
        # when the snake hits the food it refresh the location of food

        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect the collision of wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        scoreboard.game_over()
    # Detect the collision with wall
    for segments in snake.segments[1:]:  # or
        # if segments == snake.head:
        #     pass
        if snake.head.distance(segments) < 10:
            game_is_on = False
            scoreboard.game_over()

screen.exitonclick()

# Practice
# turtle_1 = Turtle()
#
# turtle_1.shape("square")
# turtle_1.color("white")
# # turtle_1.penup()
# #turtle_1.shapesize(2, 2)
# turtle_1.goto(x=0, y=0)
#
# turtle_2 = Turtle()
#
# turtle_2.shape("square")
# turtle_2.color("white")
# # turtle_2.penup()
# #turtle_2.shapesize(2, 2)
# turtle_2.goto(x=-20, y=0)


# turtle_3 = Turtle()
#
# turtle_3.shape("square")
# turtle_3.color("white")
# # turtle_3.penup()
# # turtle_3.shapesize(2, 2)
# turtle_3.goto(x=-40, y=0)
