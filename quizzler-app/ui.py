from tkinter import *
from quiz_brain import QuizBrain
import os

THEME_COLOR = "#375362"

class QuizInterface:
  
  def __init__(self, quiz_brain: QuizBrain ):
    self.quiz = quiz_brain
    
    self.window = Tk()
    self.window.title("Quizzler")
    self.window.config(bg=THEME_COLOR, padx=20, pady=20)
    
    self.score_label = Label(text="SCORE: 0", fg="white", bg=THEME_COLOR, font=("Arial", 28))
    self.score_label.grid(row=0, column=1)
    
    wrong_image = PhotoImage(file=f"{os.getcwd()}/quizzler-app/images/false.png")
    self.wrong = Button(image=wrong_image, highlightbackground=THEME_COLOR, command=self.false)
    self.wrong.grid(column=1, row=2)
    
    right_image = PhotoImage(file=f"{os.getcwd()}/quizzler-app/images/true.png")
    self.right = Button(image=right_image, highlightbackground=THEME_COLOR, command=self.true)
    self.right.grid(column=0, row=2)
    
    self.canvas = Canvas(height=300, width=400, highlightthickness=0, bg="white")
    self.question = self.canvas.create_text(
      (200, 150),
      text="Question", 
      fill=THEME_COLOR,
      font=("Arial", 20, "italic"),
      width=350
      )
    self.canvas.grid(column=0, row=1, columnspan=2, pady=30)
    
    self.get_next_question()
    
    self.window.mainloop()

  def get_next_question(self):
    self.canvas.config(bg='white')
    if self.quiz.still_has_questions():
      self.score_label.config(text=f"SCORE: {self.quiz.score}")
      q_text = self.quiz.next_question()
      self.canvas.itemconfig(self.question, text=q_text)
    else:
      self.canvas.itemconfig(self.question, text="Congratulations! You completed the quiz!")
      self.right.config(state="disabled")
      self.wrong.config(state="disabled")
    
  def true(self):
    self.give_feedback(self.quiz.check_answer("True"))
    
  def false(self):
    self.give_feedback(self.quiz.check_answer("False"))

  def give_feedback(self, is_right):
    if is_right:
      self.canvas.config(bg='green2')
    else:
      self.canvas.config(bg='firebrick1')
    self.window.after(1000, self.get_next_question)
