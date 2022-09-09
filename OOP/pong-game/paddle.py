from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, x):
    super().__init__()
    self.x = x
    self.penup()
    self.goto(x, 0)
    self.color("white")
    self.shape("square")
    self.shapesize(5, 1)
    # self.shapesize(1, 5)
    # self.setheading(90)
    
    
  def move_up(self):
    if self.ycor() < 245:
      self.goto(self.xcor(), self.ycor() + 20)
      # self.setheading(90)
      # self.forward(20)
    
  def move_down(self):
    if self.ycor() > -225:
      self.goto(self.xcor(), self.ycor() - 20)
      # self.setheading(270)
      # self.forward(20)