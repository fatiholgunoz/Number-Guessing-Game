#Number Guessing Game Objectives:

# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from random import randint
CORRECT_NUMBER = randint(1,100)

print("Welcome to the Number Guessing Game!")
print("The correct number is between 1 and 100.")
difficulty = input("Choose a difficulty, Type in 'easy' or 'hard': ")

if difficulty == "easy":
  trials = 10
elif difficulty == "hard":
  trials = 5

while trials > 0:
  print(f"\nYou have {trials} guesses remaining.")
  guess = int(input("Make a guess: "))
  if guess == CORRECT_NUMBER:
    print(f"\nGot it! The number was {CORRECT_NUMBER}.")
    break
  elif guess < CORRECT_NUMBER:
    print("Too low. ")
    trials -= 1
  elif guess > CORRECT_NUMBER:
    print("Too high. ")
    trials -= 1

if trials == 0:
  print("You have ran out of guesses, you lose.")