from turtle import Screen, Turtle
import random 

race_on = False
screen = Screen()
screen.setup(500, 400)

colours = ["red", "orange", "yellow", "green", "blue", "purple"]
  
user_bet = screen.textinput("Make your bet!", "Choose a winning turtle (enter a colour): ")

if user_bet:
  race_on = True
  
turtles = []
y = 130

for c in colours:
  turtle = Turtle('turtle')
  turtle.color(c)
  turtle.penup()
  turtle.goto(-230, y)
  y -= 50
  turtles.append(turtle)

while race_on:
  for turtle in turtles:
    if turtle.xcor() > 220:
      race_on = False
      if user_bet == turtle.pencolor():
        print("You have won")
      else:
        print("You lost")
      break      
    turtle.forward(random.randint(0,10))
   

  


  


screen.exitonclick()