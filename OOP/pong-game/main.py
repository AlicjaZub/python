from turtle import Screen
from paddle import Paddle
from line import Line
from ball import Ball
from score import Score

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
game_on = True
screen.title("PONG")
screen.tracer(0)

line = Line()
ball = Ball()
score = Score()

paddle_l = Paddle(-370)
paddle_r = Paddle(360)

screen.listen()
screen.onkey(paddle_l.move_up, "w")
screen.onkey(paddle_l.move_down, "s")
screen.onkey(paddle_r.move_up, "Up")
screen.onkey(paddle_r.move_down, "Down")

while game_on:

  ball.move()
  screen.update()
  # ball bounces of the walls
  if ball.ycor() > 290 or ball.ycor() < -290:
    ball.bounce_y()
  
  # ball bounces of the paddles
  if ball.distance(paddle_l) < 45 and ball.xcor() < -350:
    ball.bounce_x()
  elif ball.distance(paddle_r) < 45 and ball.xcor() > 340:
    ball.bounce_x()
  
  # ball misses the paddles
  if ball.distance(paddle_l) > 20 and ball.xcor() > 400:
    score.cal_score('right')
    ball.reset()
  elif ball.distance(paddle_r) > 20 and ball.xcor() < -410:
    score.cal_score('left')
    ball.reset()
    
  if score.score_l == 5 or score.score_r == 5:
    line.clear()
    score.game_over()
    game_on = False

  

screen.exitonclick()