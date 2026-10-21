#!/usr/bin/python

# Make your own "Choose Your Own Adventure" game. Use conditionals such as if, else, and elif statements to lay out the logic and the story's path in your program.

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 



#Write your code below this line 👇
left_or_right = input("You encounter a fork in the road. Do you go left or right?\n").lower()

if left_or_right == "right":
    print("You fell into a hole. Game Over\n")
else:
  swim_or_wait = input("You reach a body of water. Do you wait or swim?\n").lower()
  
  if swim_or_wait == "swim":
    print("Attacked by a vicious shark! Game Over\n")
  else:
    door = input("After some time you are transported. \nYou are confronted with three large doors - one blue, one red, and one yellow. \nWhich door do you enter? (blue, red, or yellow)\n").lower()
    if door == "blue":
      print("Eaten by cave trolls. Game over\n")
    elif door == "red":
      print("Fell into a fire pit. Game Over.")
    elif door == "yellow":
      print("You found the treasure. You Win!")
    else:
      print("You didn't choose a door and were swallowed up by an unknown creaure in the darkness. Game Over.")

