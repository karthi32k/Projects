from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
tim.color("dark green")
tim.width(10)
#tim.filling("black")
#pratice
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.left(100)
tim.right(90)
tim.speed()
tim.home()

#Draw the Square:Method1

# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.home()

#Draw the Square:Method2
# for _ in range(4):
#     tim.forward(100)
#     tim.right(90)

#Installing modules from  large packages

# import heroes
# print(heroes.gen())

#

# for _ in range(15):
#     tim.forward(10)
#     tim.penup()
#     tim.forward(10)
#     tim.pendown()
# for _ in range(2):



screen = Screen()
screen.exitonclick()