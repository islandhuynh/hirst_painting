import colorgram
from turtle import *
import random

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

colormode(255)
tim = Turtle()
tim.hideturtle()
tim.penup()
tim.speed("fastest")
tim.setposition(-300, -300)
tim.setheading(0)
tim.color(rgb_colors[random.randint(0, len(rgb_colors) - 1)])

for row in range(10):
    if row % 2 == 0:
        for _ in range(10):
            tim.dot(10, rgb_colors[random.randint(0, len(rgb_colors) - 1)])
            tim.forward(30)
        tim.dot(10, rgb_colors[random.randint(0, len(rgb_colors) - 1)])
    else:
        tim.left(90)
        tim.forward(30)
        tim.left(90)
        for _ in range(10):
            tim.dot(10, rgb_colors[random.randint(0, len(rgb_colors) - 1)])
            tim.forward(30)
        tim.dot(10, rgb_colors[random.randint(0, len(rgb_colors) - 1)])
        tim.right(90)
        tim.forward(30)
        tim.right(90)

screen = Screen()
screen.exitonclick()
