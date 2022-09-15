from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
  
  def __init__(self):
    self.snake = []
    self.x_cor = 0
    self.create()
    self.head = self.snake[0]
    self.tail = self.snake[-1]

  def create(self):
    for x in range(3):
      self.add_cube(self.x_cor)
      self.x_cor -= 20
  
  def move(self):
    for cube_num in range(len(self.snake) - 1, 0, -1):
      new_x = self.snake[cube_num - 1].xcor()
      new_y = self.snake[cube_num - 1].ycor()
      self.snake[cube_num].goto(new_x, new_y)
    self.head.forward(20)
  
  def turn_right(self):
    if self.head.heading() != LEFT:
      self.head.setheading(RIGHT)
  
  def turn_left(self):
    if self.head.heading() != RIGHT:
      self.head.setheading(LEFT)
      
  def move_down(self):
    if self.head.heading() != UP:
      self.head.setheading(DOWN)
    
  def move_up(self):
    if self.head.heading() != DOWN:
      self.head.setheading(UP)
      
  def add_cube(self, x, y = 0):
    cube = Turtle("square")
    cube.penup()
    cube.color('white')
    cube.goto(x, y)
    self.snake.append(cube)

  def reset(self):
    for cube in self.snake:
      cube.goto(800,800)
    self.snake.clear()
    self.create()
    self.head = self.snake[0]