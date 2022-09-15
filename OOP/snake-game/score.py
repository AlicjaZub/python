from turtle import Turtle
import os

ALIGNMENT = 'center'
FONT = ('Arial', 16, 'normal')

class ScoreBoard(Turtle):
  
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.score = 0
    self.high_score = 0
    self.color("white")
    self.goto(0, 270)
    self.board()
    
    
  def cal_score(self):
    self.score += 1
    self.board()

  def board(self):
    
    with open("/Users/alicjazubel/Documents/python/OOP/snake-game/data.txt") as file:
        self.high_score = int(file.read())
    self.clear()
    self.write(f"SCORE: {self.score} HIGHEST SCORE: {self.high_score}", False, align=ALIGNMENT, font=FONT)

  def reset(self):
    if self.score > self.high_score:
      self.high_score = self.score
      with open("/Users/alicjazubel/Documents/python/OOP/snake-game/data.txt", "w") as file:
        file.write(f"{self.high_score}")
    self.score = 0
    self.board()
    