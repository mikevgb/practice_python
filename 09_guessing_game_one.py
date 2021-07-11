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

while True:
	random_num = random.randint(1,9)
	user_input = input("Please, enter a number between 1 and 9: ")
	if user_input == str("exit"):
		exit()
	if int(user_input) > random_num:
		print ("Too high")
	elif int(user_input) < random_num:
		print ("Too low")
	elif int(user_input) == random_num:
		print ("Exactly")
