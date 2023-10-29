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
    colour_levels = (r, g, b)
    return colour_levels

def draw_random():
   # colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
    direction = [0, 90, 180, 270]
    tim.speed("fastest")
    tim.width(15)
    for _ in range(200):
        tim.color(random_colour())
        tim.setheading(random.choice(direction))
        tim.shape("circle")
        tim.forward(30)


draw_random()

screen = Screen()
screen.exitonclick()