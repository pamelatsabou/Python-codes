from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
words = {}

try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    words = original_data.to_dict(orient="records")
else:
    words = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(words)
    card_front.itemconfig(card_title, text="French", fill="black")
    card_front.itemconfig(card_word, text=current_card["French"], fill='black')
    card_front.itemconfig(card_background, image=image1)
    window.after(3000, func=flip_card)


def flip_card():
    card_front.itemconfig(card_title, text="English")
    card_front.itemconfig(card_word, text=current_card["English"], fill="white")
    card_front.itemconfig(card_background, image=card_back_img)


def is_known():
    words.remove(current_card)
    next_card()
    data = pandas.DataFrame(words)
    data.to_csv("data/words to learn.csv", index=False)


window = Tk()
window.title("Flashy")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

card_front = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
image1 = PhotoImage(file="/home/pamela/Documents/Python projects/1.1 flash-card-project-start/images/card_front.png")
card_back_img = PhotoImage(file="/home/pamela/Documents/Python projects/1.1 flash-card-project-start/images/card_back.png")

card_background = card_front.create_image(400, 263, image=image1)
card_title = card_front.create_text(400, 150, text='', font=('Arial', 40, "italic"))
card_word = card_front.create_text(400, 250, text="", font=("Arial", 60, "bold"))
card_front.grid(column=0, row=0, columnspan=2)

check_image = PhotoImage(file="/home/pamela/Documents/Python projects/1.1 flash-card-project-start/images/wrong.png")
known_button = Button(image=check_image, highlightthickness=0, command=next_card)
known_button.grid(column=0, row=1)

cross_image = PhotoImage(file="/home/pamela/Documents/Python projects/1.1 flash-card-project-start/images/right.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=is_known)
unknown_button.grid(column=1, row=1)

next_card()

window.mainloop()
