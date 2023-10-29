from turtle import Screen, Turtle
from random import random

RADIUS = 200

screen = Screen()

turtle = Turtle()
turtle.shape('turtle')
turtle.shapesize(5, outline=5)
turtle.speed('fast')
turtle.width(80)

turtle.penup()
turtle.sety(-RADIUS)
turtle.pendown()

def randomize():
    turtle.pencolor(random(), random(), random())
    turtle.fillcolor(random(), random(), random())

    turtle.circle(RADIUS, extent=30)

    screen.ontimer(randomize)

randomize()

screen.exitonclick()