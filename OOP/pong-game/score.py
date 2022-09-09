from turtle import Turtle

ALIGNMENT = 'center'
FONT = ('Arial', 16, 'normal')

class Score(Turtle):
  
  def __init__(self):
    super().__init__()
    self.penup()
    self.hideturtle()
    self.score_l = 0
    self.score_r = 0
    self.color("white")
    self.goto(0, 270)
    self.board()
    
    
    
  def cal_score(self, player):
    if player == "left":
      self.score_r += 1
    else:
      self.score_l += 1
    self.board()

  def board(self):
    self.clear()
    self.goto(-200, 270)
    self.write(f"SCORE: {self.score_l}", False, align='center', font=FONT)
    self.goto(200, 270)
    self.write(f"SCORE: {self.score_r}", False, align='center', font=FONT)

  def game_over(self):
    self.goto(0, 0)
    self.pensize(10)
    if self.score_l > self.score_r:
      self.write(f"PLAYER ONE HAS WON", False, align=ALIGNMENT, font=FONT)
    else:
      self.write(f"PLAYER TWO HAS WON", False, align=ALIGNMENT, font=FONT)