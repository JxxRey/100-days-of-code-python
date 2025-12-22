# import colorgram
#
# colors = colorgram.extract("image.jpg", 6)
#
# rgb_colors = []
# for color in colors:
#     rgb_colors.append((color.rgb.r, color.rgb.g, color.rgb.b))
#
# print(rgb_colors)

import random
import turtle
from turtle import Turtle, Screen

turtle.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.pencolor("blue")
amount_to_turn = [0, 90, 180, 270]
# timmy.speed("fastest")
timmy.pensize(5)
timmy.penup()
color_list = [(229, 228, 226), (225, 223, 224), (199, 175, 118), (125, 36, 24), (187, 158, 50), (170, 105, 56)]

def turtle_hirst_art(x, y):
    for _ in range(10):
        timmy.goto(x, y)
        for _ in range(10):
            timmy.dot(20, random.choice(color_list))
            timmy.forward(50)
        y += 50

turtle_hirst_art(-250, -100)


screen = Screen()
screen.exitonclick()