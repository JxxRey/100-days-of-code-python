import turtle
from turtle import Turtle, Screen
import random



turtle.colormode(255)
timmy = Turtle()
timmy.shape("turtle")
timmy.pencolor("blue")
amount_to_turn = [0, 90, 180, 270]
timmy.speed("fastest")
timmy.pensize(5)



def turtle_random_walk():
    timmy.color(random_color())
    angle = random.choice(amount_to_turn)
    direction = random.choice([timmy.left, timmy.right])

    timmy.forward(50)
    direction(angle)


def random_color():
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)

    return r, g, b
timmy.color(random_color())

def turtle_spirograph(change_angle):
    for i in range(36):
        timmy.color(random_color())
        timmy.circle(200)
        timmy.setheading(change_angle)
        change_angle += 10





turtle_spirograph(10)

# for i in range(100):
#     turtle_random_walk()


screen = Screen()
screen.exitonclick()