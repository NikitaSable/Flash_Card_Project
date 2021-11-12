import pandas
import random
from tkinter import *

BACKGROUND_COLOR = "#B1DDC6"
french_word = {}
to_learn = {}

try:
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
    french_word = {}
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")



def random_french_word():
    global french_word, flip_time
    window.after_cancel(flip_time)
    french_word = random.choice(to_learn)
    canvas.itemconfig(card_title, text="French", fill="black")
    canvas.itemconfig(card_word, text=french_word["French"], fill="black")
    canvas.itemconfig(card_background, image=front_card)
    flip_time = window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=french_word["English"], fill="white")
    canvas.itemconfig(card_background, image=back_card)


def is_know():
    to_learn.remove(french_word)
    data = pandas.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index=False)
    random_french_word()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_time = window.after(3000, func=flip_card)

canvas = Canvas(width=800, height=526)
front_card = PhotoImage(file="images/card_front.png")
back_card = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=front_card)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_button = PhotoImage(file="images/right.png")
button = Button(image=right_button, highlightthickness=0, command=is_know)
button.grid(row=1, column=1)

wrong_button = PhotoImage(file="images/wrong.png")
button = Button(image=wrong_button, highlightthickness=0, command=random_french_word)
button.grid(row=1, column=0)

random_french_word()

window.mainloop()
