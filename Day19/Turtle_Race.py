from turtle import Turtle, Screen
import random

colors = ["red", "orange", "pink", "green", "blue", "purple"]

screen = Screen()
screen.setup(500, 500)

user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
print(user_bet)



def add_turtles():
    turts = []
    y = -125
    for i in range(0, 6):
        turts.append(Turtle(shape="turtle"))
        turts[i].color(colors[i])
        turts[i].penup()
        turts[i].goto(-230, y)
        y += 50
    return turts



turtles = add_turtles()
the_flash = Turtle(shape="turtle")
the_flash.penup()
the_flash.color("yellow")
the_flash.goto(-230, -150)



race_on = False
if user_bet:
    race_on = True
while race_on:
    for turts in turtles:
        if turts.xcor() > 230:
            winning_color = turts.pencolor()
            if winning_color == user_bet:
                print(f"You win! The {winning_color} turtle is the winner!")
            else:
                print(f"You lost! The {winning_color} turtle is the winner!")
            race_on = False

        rand_distance = random.randint(0,10)
        turts.forward(rand_distance)
        the_flash.forward(2)



screen.exitonclick()
