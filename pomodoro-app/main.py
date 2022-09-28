import math
from tkinter import *
import os
# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
marks = ""
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset():
  global reps
  global marks
  
  window.after_cancel(timer)
  reps = 1
  marks = ""
  ticks.config(text=marks)
  title.config(text="Timer", fg=GREEN)
  canvas.itemconfig(timer_text, text="25:00")

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_countdown():
  global reps
  if reps % 8 == 0:
    count_down(LONG_BREAK_MIN * 60)
    title.config(text="Break", fg=RED)
  elif reps % 2 == 0:
    # count_down(6)
    count_down(SHORT_BREAK_MIN * 60)
    title.config(text="Break", fg=PINK)
  else:
    # count_down(10)
    count_down(WORK_MIN * 60)
    title.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
 
  min = math.floor(count/60)
  if min < 10:
    min = f"0{min}"
  sec = count % 60
  if sec < 10:
    sec = f"0{sec}"
  canvas.itemconfig(timer_text, text=f"{min}:{sec}")
  if count >= 0:
    global timer
    timer = window.after(1000, count_down, count - 1)
  else:
    global reps
    global marks
    if reps % 2 != 0:
      marks +="✓"
      ticks.config(text=marks)
    reps += 1
      
    start_countdown()

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
title.grid(column=1, row= 0)

canvas = Canvas(height=224, width=200, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file=f"{os.getcwd()}/pomodoro-app/tomato.png")
canvas.create_image(100, 112, image=tomato)
timer_text = canvas.create_text(100, 130, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="Start", highlightbackground=YELLOW, command=start_countdown)
start.grid(column=0, row=2)

reset = Button(text="Reset", highlightbackground=YELLOW, command=reset)
reset.grid(column=3, row=2)

ticks = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "bold"))
ticks.grid(column=1, row=3)

window.mainloop()