# -*- coding: utf-8 -*-
# Generate a random number between 1 and 9 (including 1 and 9). Ask the user to
# guess the number, then tell them whether they guessed too low, too high, or 
# exactly right. (Hint: remember to use the user input lessons from the very 
# first exercise)

# Extras:

# Keep the game going until the user types “exit”
# Keep track of how many guesses the user has taken, and when the game ends, 
# print this out.

import random
import os

random = random.randint(1,9)

user_input = raw_input("Please, enter a number between 1 and 9: ")

if user_input == str("exit"):
	exit()
if int(user_input) > random:
	print ("Too high")
if int(user_input) < random:
	print ("Too low")
if int(user_input) == random:
	print ("Exactly")
os.system("python 09_guessing_game_one.py 1")