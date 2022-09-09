from turtle import Turtle
import time

class Ball(Turtle):
  
  def __init__(self):
    super().__init__()
    self.shape("circle")
    self.color("turquoise")
    self.penup()
    self.x_move = 1
    self.y_move = 1
    
  def move(self):
    # print(self.ycor())
    # if 390 > self.xcor() > -390 and 290 > self.ycor() > -290:
    new_x = self.xcor() + self.x_move
    new_y = self.ycor() - self.y_move
    self.goto(new_x, new_y)

  def bounce_y(self):
    self.y_move *= -1
  
  def bounce_x(self):
    self.x_move *= -1
    
  def reset(self):
    self.goto(0, 0)
    time.sleep(1)
