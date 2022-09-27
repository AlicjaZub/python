import turtle
import os
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = f"{os.getcwd()}/files/states_quiz/blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

guessed = []

# def get_mouse_click_coor(x, y):
#   print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)


data = pandas.read_csv(f"{os.getcwd()}/files/states_quiz/50_states.csv")
states = data.state.tolist()

def not_guessed(states, guessed):
  not_guessed = list((set(states) | set(guessed)) - (set(states) & set(guessed)))
  data = pandas.DataFrame(not_guessed)
  data.to_csv(f"{os.getcwd()}/files/states_quiz/states_to_learn.csv")
  
while len(guessed) < 50:
  answer = screen.textinput(title=f" {len(guessed)}/50 Guess the state", prompt="What's another state's name?")
  answer = answer.lower().capitalize()
  if answer == "Exit":
    not_guessed(states, guessed)
    break
    
  if answer in states:
    state = turtle.Turtle()
    state.hideturtle()
    state.penup()
    state_data = data[data.state == answer]
    state.goto(int(state_data.x), int(state_data.y))
    state.write(answer)
    guessed.append(answer)






turtle.mainloop()

