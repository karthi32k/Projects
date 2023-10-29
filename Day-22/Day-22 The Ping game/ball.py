from turtle import Turtle


class Ball(Turtle):  # it is going to inherit to the turtle class

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        # self.shapesize(stretch_wid=1, stretch_len=1)  # pixel is 20X20
        self.penup()
        self.x_move_ball = 10
        self.y_move_ball = 10
        self.move_speed = 0.1
    def move_ball(self):
        new_x = self.xcor() + self.x_move_ball  # 1 represents 1 pixel
        new_y = self.ycor() + self.y_move_ball
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_move_ball *= -1  # Reversing the Y direction

    def bounce_x(self):
        self.x_move_ball *= -1  # Reversing the X direction
      #  self.move_speed *= 0.9  # it 0.5 * 0.1 = 0.05 U can choose it 0.5 or something

    def reset_position(self):
        self.goto(0, 0)
       # self.speed(0.1)  # it reset the actual speed
        self.bounce_x()


