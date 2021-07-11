# -*- coding: utf-8 -*-

# Create a program that will play the “cows and bulls” game with the user. The
# game works like this:

# Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
# For every digit that the user guessed correctly in the correct place, they 
# have a “cow”. For every digit the user guessed correctly in the wrong place 
# is a “bull.” Every time the user makes a guess, tell them how many “cows” 
# and “bulls” they have. Once the user guesses the correct number, the game 
# is over. Keep track of the number of guesses the user makes throughout the
# game and tell the user at the end.

# Say the number generated by the computer is 1038. An example interaction
# could look like this:

#   Welcome to the Cows and Bulls Game! 
#   Enter a number: 
#   >>> 1234
#   2 cows, 0 bulls
#   >>> 1256
#   1 cow, 1 bull
#   ...

# Until the user guesses the number.

import random

def comp(input_number, my_num):
	count = [0,0]
	for i in range(len(my_num)):
		if my_num[i] == input_number[i]:
			count[0] += 1
	for x in range(len(my_num)):
		if input_number[x] in my_num and input_number[x] != my_num[x]:
			count[1] += 1
	return (count)

if __name__=="__main__":
	my_num = str(random.randint(1000, 9999))
	print (my_num)
	while True:
		input_number = input("Enter a number: ")
		counter2 = comp(input_number, my_num)
		print(str(counter2[1]) + " cows, " + str(counter2[0]) + " bulls")
		if my_num == input_number:
			print("You win")
			break
		