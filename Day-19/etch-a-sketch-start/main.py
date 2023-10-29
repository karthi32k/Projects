from turtle import Turtle, Screen
import random

tim = Turtle(shape="turtle")
screen = Screen()

colors = ["red", "Orange", "green", "blue", "purple", "dark blur", "sky blue", "sea green"]

random_color = random.choice(colors)

tim.color(random_color)


def move_forwards():
    tim.forward(50)


def move_backward():
    tim.backward(50)


def turn_left():
    tim.left(20)
    tim.heading()


def turn_right():
    tim.right(20)
    tim.heading()


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    #tim.pendown()


screen.listen()

screen.onkey(move_forwards, "Up")
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Left", fun=turn_left)
screen.onkey(key="Right", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()

