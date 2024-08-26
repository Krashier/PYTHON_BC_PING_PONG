from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.speed("fastest")
        self.color("white")
        self.penup()
        self.x = 10
        self.y = 10

    def move_ball(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x,new_y)

    def up_down_bounce(self):
        self.y *= -1

    def bounce_pad(self):
        self.x *= -1