from art import logo
from game_data import data
import random


def choose_person(choices):
    choice = random.choice(choices)
    choices.remove(choice)
    return choice


def choice(choice_a, choice_b):
    print("Who has more followers?")
    return input(f"A: {choice_a['name']} or B: {choice_b['name']}? ").lower()


def score(followers_a, followers_b, guess, points):
    if (followers_a > followers_b
            and guess == "a") or (followers_a < followers_b and guess == "b"):
        return True
    elif (followers_a < followers_b
          and guess == "a") or (followers_a > followers_b and guess == "b"):
        print(f"You lose. You managed to guess {points} rounds!")
        return False

def game():
  choices = list(range(0, 50))
  points = 0
  
  choice_a = data[choose_person(choices)]
  choice_b = data[choose_person(choices)]
  
  followers_a = choice_a['follower_count']
  followers_b = choice_b['follower_count']
  
  game_on = True
  print(logo)
  while game_on:
      guess = choice(choice_a, choice_b)
      game_on = score(followers_a, followers_b, guess, points)
      if game_on:
          print("Correct")
          points += 1
          if points == 49:
              print("You have won!")
              break
          if followers_a < followers_b:
              choice_a = choice_b
              followers_a = choice_a['follower_count']
          choice_b = data[choose_person(choices)]
          followers_b = choice_b['follower_count']
      else:
        return input("Do you want to play again? 'y' or 'n' ? ").lower()

again = game()
while again == 'y':
  again = game()