from turtle import Screen
from Pads import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


screen = Screen()
screen.setup(800,600)
screen.bgcolor("black")
screen.title("Ping Pong")
screen.tracer(0)

r_pad = Paddle((350,0))
l_pad = Paddle((-350,0))
square = Ball()
scoreboard = Scoreboard()

default_time = 0.1

screen.listen()
screen.onkey(l_pad.up,"w")
screen.onkey(l_pad.down,"s")
screen.onkey(r_pad.up,"Up")
screen.onkey(r_pad.down,"Down")


game_on = True

while game_on:
    square.move_ball()
    if square.ycor() > 280 or square.ycor() < -280:
        square.up_down_bounce()
    if square.distance(r_pad) < 50 and square.xcor() > 320 or square.distance(l_pad) < 50 and square.xcor() < -320:
        square.bounce_pad()
        default_time -= 0.01
    if square.xcor() > 380:
        scoreboard.l_point()
    elif square.xcor() < -380:
        scoreboard.r_point()
    if square.xcor() > 380 or square.xcor() < -380: 
        square.setpos(0,0)
        default_time = 0.1
        square.bounce_pad()
        square.move_ball()
    screen.update()
    time.sleep(default_time)
    
screen.exitonclick()