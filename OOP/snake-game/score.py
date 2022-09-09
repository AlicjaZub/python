from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 16, 'normal')

class ScoreBoard(Turtle):
  
  def __init__(self):
    super().__init__()
    self.hideturtle()
    self.score = 0
    self.color("white")
    self.goto(0, 270)
    self.board()
    
    
  def cal_score(self):
    self.score += 1
    self.board()

  def board(self):
    self.clear()
    self.write(f"SCORE: {self.score}", False, align=ALIGNMENT, font=FONT)

  def game_over(self):
    self.goto(0, 0)
    self.write("GAME OVER", False, align=ALIGNMENT, font=FONT)