from turtle import Turtle
pads = []

class Paddle(Turtle):
    def __init__(self,pos):
        super().__init__()
        self.shape("square")
        self.speed(0)
        self.penup()
        self.setheading(90)
        self.shapesize(1,5)
        self.setposition(pos)
        self.color("white")

    def up(self):
        self.forward(20)
    def down(self):
        self.forward(-20)
