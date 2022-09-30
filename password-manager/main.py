from tkinter import *
from tkinter import messagebox
import os
from random import choice, randint, shuffle
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_passsword():

  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  password_list = [choice(letters) for _ in range(randint(8, 10))]
  password_list += [choice(symbols) for _ in range(randint(2, 4))]
  password_list += [choice(numbers) for _ in range(randint(2, 4))]

  shuffle(password_list)
  password.delete(0, END)
  new_password = "".join(password_list)
  password.insert(END, new_password)
  pyperclip.copy(new_password)

# ---------------------------- SEARCH FOR DATA ------------------------------- #

def search():
  w = website.get().lower()
  try:
    with open(f"{os.getcwd()}/password-manager/data.json", "r") as file:
      data = json.load(file)
  except FileNotFoundError:
      messagebox.showinfo(message="You don't have any passwords yet")
  else:
    if w == "":
      pass
    else:
      try:
        messagebox.showinfo(message=f"The details for the {w.capitalize()} website:\nEMAIL: {data[w]['email']}\n  PASSWORD: {data[w]['password']}\n")
      except KeyError:
        messagebox.showinfo(message=f"No data for this website stored")

# ---------------------------- SAVE PASSWORD ------------------------------- #

def save_data():
  w = website.get().lower()
  e = email.get()
  p = password.get()
  new_data = { w: {
    "email": e,
    "password": p,
  }}
  
  if len(w) == 0 or len(p) == 0:
    messagebox.showinfo(title="Oops", message="Please make sure you haven't left any fields empty")
  else:
    try:
      with open(f"{os.getcwd()}/password-manager/data.json", "r") as file:
        data = json.load(file)
        if data[w]:
          confirm = messagebox.askokcancel(title=w, message=f"You already have a password stored for this website - would you like to overwrite it?")
    except FileNotFoundError:
      with open(f"{os.getcwd()}/password-manager/data.json", "w") as file:
        json.dump(new_data, file, indent=2)
    else:
      if confirm:
        data.update(new_data)
        with open(f"{os.getcwd()}/password-manager/data.json", "w") as file:
          json.dump(data, file, indent=2)
      else:
        pass
    finally:
      website.delete(0, END)
      password.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password manager")
window.config(padx=40, pady=40)

# logo
canvas = Canvas(height=200, width=200, highlightthickness=0)
logo = PhotoImage(file=f"{os.getcwd()}/password-manager/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

# labels
website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

# inputs
website = Entry(width=18)
website.grid(column=1, row=1)
website.focus()
email = Entry(width=34)
email.grid(column=1, row=2, columnspan=2)
email.insert(END, string="alicja@madebyon.com")
password = Entry(width=18)
password.grid(column=1, row=3)

# buttons
search_button = Button(text="Search", width=12, command=search)
search_button.grid(column=2, row=1)
generate_passwrod_button = Button(text="Generate Password", width=12, command=generate_passsword)
generate_passwrod_button.grid(column=2, row=3)
add_button = Button(text="Add", width=32, command=save_data)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()