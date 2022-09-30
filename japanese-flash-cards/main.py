from tkinter import *
import os
from random import choice
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ---------------------------- LOGIC ------------------------------- #

def get_data():
  try:
    data = pandas.read_csv(f"{os.getcwd()}/japanese-flash-cards/words_to_learn.csv")
  except FileNotFoundError:
    data = pandas.read_csv(f"{os.getcwd()}/japanese-flash-cards/words.csv")
  return data.to_dict(orient="records")
  # return [[row.word, row.translation] for (index, row) in data.iterrows()]
  
def get_word():
  global current_card, flip_timer
  window.after_cancel(flip_timer)
  current_card = choice(data)
  print(current_card)
  canvas.itemconfig(title, text="Japanese", fill="black")
  canvas.itemconfig(word, text=current_card["japanese"], fill="black")
  canvas.itemconfig(background, image=card_front)
  window.after(3000, flip)

def correct():
  data.remove(current_card)
  get_word()
  new_data = pandas.DataFrame(data)
  new_data.to_csv(f"{os.getcwd()}/japanese-flash-cards/words_to_learn.csv", index=False)
  
def flip():
  global current_card
  canvas.itemconfig(background, image=card_back)
  canvas.itemconfig(word, text=current_card["english"], fill="white")
  canvas.itemconfig(title, text="English", fill="white")

# ---------------------------- UI ------------------------------- #

window = Tk()
window.title("Flash cards")
window.config(padx=40, pady=40, bg=BACKGROUND_COLOR)
data = get_data()

# card
canvas = Canvas(height=526, width=800, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front = PhotoImage(file=f"{os.getcwd()}/japanese-flash-cards/images/card_front.png")
card_back = PhotoImage(file=f"{os.getcwd()}/japanese-flash-cards/images/card_back.png")
background = canvas.create_image(400, 263, image=card_front)
word = canvas.create_text(400, 263, font=("Ariel", 60, "bold"))
title = canvas.create_text(400, 150, text="Japanese", font=("Ariel", 40, "italic"))
canvas.grid(column=0, row=0, columnspan=2)

# buttons
wrong_image = PhotoImage(file=f"{os.getcwd()}/japanese-flash-cards/images/wrong.png")
wrong = Button(image=wrong_image, highlightbackground=BACKGROUND_COLOR, command=get_word)
wrong.grid(column=0, row=1)

right_image = PhotoImage(file=f"{os.getcwd()}/japanese-flash-cards/images/right.png")
right = Button(image=right_image, highlightbackground=BACKGROUND_COLOR, command=correct)
right.grid(column=1, row=1)

flip_timer = window.after(3000, flip)
get_word()

window.mainloop()
