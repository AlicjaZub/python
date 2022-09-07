from turtle import Screen, Turtle

screen = Screen()
turtle = Turtle()

def move_forwards():
  turtle.forward(20)
  
def move_right():
  turtle.right(15)
  turtle.forward(20)
  
def move_left():
  turtle.left(15)
  turtle.forward(20)
  
def move_down():
  turtle.setheading(270)
  turtle.forward(20)
  
def move_up():
  turtle.setheading(90)
  turtle.forward(20)
  
screen.listen()
screen.onkey(move_forwards, 'space')
screen.onkey(move_up, 'Up')
screen.onkey(move_down, 'Down')
screen.onkey(move_right, 'Right')
screen.onkey(move_left, 'Left')
screen.onkey(turtle.reset, 'c')
screen.exitonclick()