from game_data import data
import random


def choose_person(choices):
    choice = random.choice(choices)
    choices.remove(choice)
    return choice

def game():
    print("Who has more followers?")
    return input(f"A: {choice_a['name']} or B: {choice_b['name']}? ").lower()


def score():
    if (followers_a > followers_b and guess == "a") or (followers_a < followers_b and guess == "b"):
        return True
    elif (followers_a < followers_b
          and guess == "a") or (followers_a > followers_b and guess == "b"):
        print(f"You lose. You managed to guess {points} rounds!")
        return False

choices = list(range(0, 50))
points = 0

choice_a = data[choose_person(choices)]
choice_b = data[choose_person(choices)]

followers_a = choice_a['follower_count']
followers_b = choice_b['follower_count']

game_on = True
while game_on:
    guess = game()
    game_on = score()
    if game_on:
        print("Correct")
        points += 1
        if followers_a < followers_b:
            choice_a = choice_b
            followers_a = choice_a['follower_count']
        choice_b = data[choose_person(choices)]
        followers_b = choice_b['follower_count']
