
import random
import turtle as t
from turtle import Screen

tim = t.Turtle()
t.colormode(255)

#To generate the random colour
def random_colour():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    colour = (r, g, b)
    return colour

tim.speed("fastest")

def spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_colour())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)
        tim.circle(100)
spirograph(5)



screen = Screen()
screen.exitonclick()