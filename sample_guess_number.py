#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
from art import logo
import random

def game_level(level):
  if level == "easy":
     guess = 10
  else:
     guess = 5
  return guess


print(logo)


number = random.randint(0,101)


print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
level = input("Choose a difficulty. Type 'easy' or 'hard': ")
life = game_level(level)

def game_start(number, life):
  while life != 0:
    user_pick = int(input("Guess the number: "))
    if user_pick > number:
      print("Too high")
      life -= 1
      print(f"You have {life} attempts remaining to guess the number.")
      if life == 0:
        print("You've run out of guesses, you lose.")
    elif user_pick < number:
      print("Too low")
      life -= 1
      if life == 0:
        print("You've run out of guesses, you lose.")
      print(f"You have {life} attempts remaining to guess the number.")
    else:
      print("Congrats! you pick the correct number!")
      break

game_start(number, life)




