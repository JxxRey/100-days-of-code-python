import turtle
from turtle import Turtle
import pandas
image = "blank_states_img.gif"

screen = turtle.Screen()
screen.title("U.S. States Game")
screen.addshape(image)

image_turtle = Turtle()
image_turtle.shape(image)


data = pandas.read_csv("50_states.csv")
states = data["state"].to_list()
x_cor = data["x"].to_list()
y_cor = data["y"].to_list()

states_guessed = []
states_to_learn = []
correct_guess = 0

game_on = True
while game_on:
    answer_state = screen.textinput(title=f"{correct_guess}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == "Exit":
        break

    for state in states:
        if state == answer_state:
            states_guessed.append(state)
            correct_guess += 1
            index_for_cor_lists = states.index(answer_state)
            turtle.penup()
            turtle.hideturtle()
            turtle.goto(x_cor[index_for_cor_lists], y_cor[index_for_cor_lists])
            turtle.write(answer_state, font=("Arial", 12, "normal"))

for state in states:
    if state not in states_guessed:
        states_to_learn.append(state)

states_to_learn = pandas.DataFrame(states_to_learn)

states_to_learn.to_csv("states_to_learn")

print(states_to_learn)