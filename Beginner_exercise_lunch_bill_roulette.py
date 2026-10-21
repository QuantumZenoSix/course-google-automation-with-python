#!/usr/bin/python


# === Instructions ===

# You are going to write a program which will select a random name from a list of (comma-separated) names. The person selected will have to pay for everybody's food bill.

# Important: You are not allowed to use the choice() function.



# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
import random

# person_who_will_pay = random.choice(name) --> A non-manual solution
last_idx = len(names) - 1
rand_idx = random.randint(0, last_idx)
print(f"{names[rand_idx]} is going to buy the meal today!")

import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇

def printArt(choice):
  if choice == 0:
    print(rock + "Rock\n")
  elif choice == 1:
    print(paper + "Paper\n")
  elif choice == 2:
    print(scissors + "Scissors\n")

player_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")

# Check to make sure we are passing in a integer
try:
  player_choice = int(player_choice)
except ValueError:
  print("Invalid Choice. Please choose again.")

# Print player Art
print("=== Player choice === ")
printArt(player_choice)

# AI Choice
print("=== Machine choice === ")
ai_choice = random.randint(0,2)
printArt(ai_choice)

if player_choice == ai_choice:
  print("Tie Game!")
elif player_choice == 0:
    if ai_choice == 1:
      print("Paper beats rock. Machine Wins!")
    elif ai_choice == 2:
      print("Rock beats Scissors.You Win!")
elif player_choice == 1:
    if ai_choice == 0:
      print("Paper beats rock. You Win!")
    elif ai_choice == 2:
      print("Scissors beats paper. Machine Wins!")
elif player_choice == 2:
    if ai_choice == 0:
      print("Rock beats Scissors. Machine Wins!")
    elif ai_choice == 1:
      print("Scissors Paper.You Win!")

# Really Cool Alternative I found...

# pics = [rock, paper, scissors]
# print(pics[your_choice])
 
# comp_choice = random.randint(0,2)
# print(f"Computer chose:\n{pics[comp_choice]}")
 
# winning_matrix = [
#   ["Draw", "You Lose", "You Win"],
#   ["You Win", "Draw", "You Lose"],
#   ["You Lose", "You Win", "Draw"]
# ]
# print(winning_matrix[your_choice][comp_choice])
