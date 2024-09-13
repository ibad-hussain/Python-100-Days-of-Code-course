# EXERCISE 5 - SNAKE WATER GUN GAME
# Problem Statement: Snake Water Gun game is a variation of the children's game "rock-paper-scissors" where players use hand gestures to represent a snake, water, or a gun. The GUN beats the SNAKE, the WATER beats the GUN, and the SNAKE beats the WATER. Write a python program to create a Snake Water Gun game in Python using if-else statements. Do not create any fancy GUI. Use proper functions to check for win.



import random
import time
from time import sleep

print("Welcome to the SNAKE WATER GUN game ...\n")
sleep(2)
print("The rules are:\n1) SNAKE will beat WATER but will be defeated by GUN\n2) WATER will beat GUN but will be defeated by SNAKE\n3) GUN will beat SNAKE but will be defeated by WATER\n4) 1 point if Draw\n5) 2 points if You Won\n")
print("-------------------------")
print(" ")
sleep(5)

name = input("Enter your name: ")
sleep(2)
print("Lets get started !")
print(" ")
sleep(1)
print("-------------------------")
print(" ")
sleep(2)

points = 0

while True:
  user = str(input("Enter\n0 for SNAKE\n1 for WATER\n2 for GUN\n"))
  comp = str(random.randint(0, 2))
  
  validInput = ["0", "1", "2"]
 
  if user not in validInput:
    sleep(2)
    print("\nGame Over!!!\nInvalid input")
    sleep(1)
    print(" ")
    print("-------------------------")
    print(" ")
    sleep(1)
    print(f"You got {points} points.")
    print("Thanks for playing !!!")
    break
    
  print(f"\n{name}'s Turn")
  if user == "0":
    print("0 : SNAKE")
  elif user == "1":
    print("1 : WATER")
  else:
    print("2 : GUN")
  
  time.sleep(2)
  
  print("Computer's Turn")
  if comp == "0":
    print("0 : SNAKE")
  elif comp == "1":
    print("1 : WATER")
  else:
    print("2 : GUN")

  time.sleep(1)
  print(" ")

  if user=="0" and comp=="0":
    print("SNAKE vs SNAKE")
    print("Draw\n")
    sleep(1)
    print("-------------------------")
    print(" ")
    sleep(1)
    points = points + 1
  elif user=="0" and comp=="1":
    print("SNAKE vs WATER")
    print("You Won\n")
    sleep(1)
    print("-------------------------")
    print(" ")
    sleep(1)
    points = points + 2
  elif user=="0" and comp=="2":
    print("SNAKE vs GUN")
    print("You Lost\n")
    sleep(1)
    print("-------------------------")
    print(" ")
    sleep(1)
    print("Game Over!")
    print(f"You got {points} points.")
    print("Thanks for playing !!!")
    break
  elif user=="1" and comp=="0":
    print("WATER vs SNAKE")
    print("You Lost\n")
    sleep(1)
    print("-------------------------")
    print(" ")
    sleep(1)
    print("Game Over!")
    print(f"You got {points} points.")
    print("Thanks for playing !!!")
    break
  elif user=="1" and comp=="1":
    print("WATER vs WATER")
    print("Draw\n")
    sleep(1)
    print("-------------------------")
    print(" ")
    sleep(1)
    points = points + 1
  elif user=="1" and comp=="2":
    print("WATER vs GUN")
    print("You Won\n")
    sleep(1)
    print("-------------------------")
    print(" ")
    sleep(1)
    points = points + 2
  elif user=="2" and comp=="0":
    print("GUN vs SNAKE")
    print("You Won\n")
    sleep(1)
    print("-------------------------")
    print(" ")
    sleep(1)
    points = points + 2
  elif user=="2" and comp=="1":
    print("GUN vs WATER")
    print("You Lost\n")
    sleep(1)
    print("-------------------------")
    print(" ")
    sleep(1)
    print("Game Over!")
    print(f"You got {points} points.")
    print("Thanks for playing !!!")
    break
  else:
    print("GUN vs GUN")
    print("Draw\n")
    sleep(1)
    print("-------------------------")
    print(" ")
    sleep(1)
    points = points + 1