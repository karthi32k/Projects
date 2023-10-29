import random
import turtle as t
from turtle import Screen

tim = t.Turtle()

#Draw the shapes:
colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray", "SeaGreen"]
# colours = ['yellow', 'cyan', 'red', 'light blue', 'pink', 'blue', 'purple', 'green', 'orange']
def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape_side_n in range(3,11):
    tim.color(random.choice(colours))
    tim.speed()
    tim.width(8)
    draw_shape(shape_side_n)




# My stupid method

#from turtle import Turtle, Screen
#import random

#tim = Turtle()

#def shapes():
#
#     def triangle():
#         for _ in range(3):
#             tim.color("orange")
#             tim.forward(100)
#             tim.right(120)
#         # tim.forward(100)
#         # tim.home()
#     triangle()
#
#     def square():
#         for _ in range(4):
#             tim.color("red")
#             tim.forward(100)
#             tim.right(90)
#     square()
#
#     def pentagon():
#         for _ in range(5):
#             tim.color("blue")
#             tim.forward(100)
#             tim.right(72)
#     pentagon()
#
#     def hexagon():
#         for _ in range(6):
#             tim.color("sky blue")
#             tim.forward(100)
#             tim.right(60)
#     hexagon()
#
#     def heptagon():
#         for _ in range(7):
#             tim.color("dark blue")
#             tim.forward(100)
#             tim.right(51.4)
#     heptagon()
#
#     def octagon():
#         for _ in range(8):
#             tim.color("purple")
#             tim.forward(100)
#             tim.right(45)
#     octagon()
#
#     def ponagon():
#         for _ in range(9):
#             tim.color("brown")
#             tim.forward(100)
#             tim.right(40)
#     ponagon()
#
#     def decagon():
#         for _ in range(10):
#             tim.color("black")
#             tim.forward(100)
#             tim.right(36)
#     decagon()


# shapes()

#

screen = Screen()
screen.exitonclick()