from turtle import Screen
import time
from snake import Snake
from food import Food
from score import ScoreBoard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
snake = Snake()
food = Food()
score = ScoreBoard()

game_on = True

screen.listen()
screen.onkey(snake.move_up, "Up")
screen.onkey(snake.move_down, "Down")
screen.onkey(snake.turn_right, "Right")
screen.onkey(snake.turn_left, "Left")

while game_on:
  screen.update()
  time.sleep(0.1)
  snake.move()

  if snake.head.distance(food) < 15:
    score.cal_score()
    food.refresh()
    snake.add_cube(snake.tail.xcor(),snake.tail.ycor())
    
  if snake.head.xcor() > 285 or snake.head.ycor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() < -285:
    score.reset()
    snake.reset()

  for cube in snake.snake[1:]:
    if snake.head.distance(cube) < 15:
      score.reset()
      snake.reset()
      
screen.exitonclick()
