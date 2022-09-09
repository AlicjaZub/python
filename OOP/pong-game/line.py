from turtle import Turtle

class Line(Turtle):
  
  def __init__(self):
    super().__init__()
    self.goto(0, 300)
    self.color('white')
    self.pensize(8)
    self.draw()
    
  def draw(self):
    for n in range(10):
      self.setheading(270)
      self.forward(30)
      self.penup()
      self.forward(30)
      self.pendown()
  