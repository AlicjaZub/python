import turtle as t
from random import choice, randint

screen = t.Screen()
screen.setworldcoordinates(-1, -1, screen.window_width() - 1, screen.window_height() - 1)
turtle = t.Turtle()
turtle.shape('turtle')
# turtle.pensize(5)
t.colormode(255)
turtle.speed('fastest')
turtle.home()

def square():
  for x in range(4):
    for n in range(15):
      turtle.forward(10)
      turtle.penup()
      turtle.forward(10)
      turtle.pendown()
    turtle.right(90)

# square()

# for x in range(3,29):
#   turtle.color(choice(colours))
#   for y in range(x):
#     turtle.forward(35)
#     turtle.right(360/x)

directions = [0, 90, 180, 270]

def random_col():
  r = randint(0,255)
  g = randint(0,255)
  b = randint(0,255)
  return (r, g, b)

def random():
  turtle.setheading(choice(directions))
  turtle.forward(30)

# for x in range(300):
#   turtle.color(random_col())
#   random()

def spirograph(gap, radius):
  for x in range(round(360/gap)):
    turtle.color(random_col())
    turtle.circle(radius)
    turtle.right(gap)
    
def dot_row(size):
  for x in range(9):
    turtle.dot(size, random_col())
    turtle.forward(79)
    turtle.dot(size, random_col())

  
def dot_rows(size):
  dot_row(size)
  turtle.left(90)
  turtle.forward(79)
  turtle.left(90)
  dot_row(size)
  turtle.right(90)
  turtle.forward(79)
  turtle.right(90)

turtle.penup()
for x in range(5):
  dot_rows(20)

screen.exitonclick()