import turtle as turtle_module
import random

turtle_module.colormode(255)
tim = turtle_module.Turtle()

tim.speed("fastest")
tim.hideturtle()
tim.penup()

color_list = [(213, 154, 96), (52, 107, 132), (179, 77, 31), (202, 142, 31), (115, 155, 171), (124, 79, 99),
              (122, 175, 156), (229, 236, 239), (226, 198, 131), (242, 247, 244), (192, 87, 108), (11, 50, 64),
              (55, 38, 19), (45, 168, 126), (47, 127, 123), (200, 121, 143), (168, 21, 29), (228, 92, 77),
              (244, 162, 160), (38, 32, 35), (2, 25, 24), (78, 147, 171), (170, 23, 18), (19, 79, 90), (101, 126, 158),
              (235, 166, 171), (177, 204, 185), (49, 62, 84)]

tim.setheading(225)
tim.fd(300)
tim.setheading(0)

number_of_dots = 100

for dot_count in range(1,  number_of_dots + 1):
    tim.dot(20, random.choice(color_list))
    tim.fd(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.fd(50)
        tim.setheading(180)
        tim.fd(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()






