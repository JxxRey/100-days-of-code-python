from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("FlashCards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Try to load words_to_learn.csv first, otherwise use french_words.csv
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    data = pandas.read_csv("./data/french_words.csv")

data_dictionary = data.to_dict(orient="records")
current_word = {}
flip_timer = None

def flip_card():
    card.itemconfig(card_background, image=card_back_image)
    card.itemconfig(top_word, text="English", fill="white")
    card.itemconfig(bottom_word, text=current_word["English"], fill="white")

def next_card():
    global current_word, flip_timer

    if flip_timer:
        window.after_cancel(flip_timer)

    current_word = random.choice(data_dictionary)

    card.itemconfig(card_background, image = card_front_image)
    card.itemconfig(top_word, text="French", fill="black")
    card.itemconfig(bottom_word, text=current_word["French"], fill="black")

    flip_timer = window.after(3000, flip_card)

def is_known():
    data_dictionary.remove(current_word)

    df = pandas.DataFrame(data_dictionary)
    df.to_csv("data/words_to_learn.csv", index=False)

    next_card()

#All Images
correct_image = PhotoImage(file="./images/right.png")
wrong_image = PhotoImage(file="./images/wrong.png")
card_front_image = PhotoImage(file="./images/card_front.png")
card_back_image = PhotoImage(file="./images/card_back.png")

#Canvas
card = Canvas(width = 800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_background = card.create_image(400, 263, image=card_front_image)
card.grid(column=0, row=0, columnspan=2)

#Buttons
correct_button = Button(image = correct_image, command=is_known)
correct_button.config(highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR)
correct_button.grid(column=1, row=1)
wrong_button = Button(image = wrong_image, command = next_card)
wrong_button.config(highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR)
wrong_button.grid(column=0, row=1)

#Text
top_word = card.create_text(400, 150, text = "Title", font = ("Ariel", 40, "italic"))
bottom_word = card.create_text(400, 263, text = "Word", font = ("Ariel", 60, "bold"))

next_card()


window.mainloop()