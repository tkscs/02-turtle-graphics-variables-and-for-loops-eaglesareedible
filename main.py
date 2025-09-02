from turtle import *

speed(1)
color("#000000")
Sides = 100

angle = (360/Sides)
for i in range(Sides):
    forward(20)
    right(angle)

exitonclick()

