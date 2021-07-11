#  -*- coding: utf-8 -*-

# This exercise is Part 3 of 3 of the Hangman exercise series. The other 
# exercises are: Part 1 and Part 2.

# You can start your Python journey anywhere, but to finish this exercise
# you will have to have finished Parts 1 and 2 or use the solutions (Part
# 1 and Part 2).

# In this exercise, we will finish building Hangman. In the game of Hangman,
# the player only has 6 incorrect guesses (head, body, 2 legs, and 2 arms)
# before they lose the game.

# In Part 1, we loaded a random word list and picked a word from it. In Part
# 2, we wrote the logic for guessing the letter and displaying that 
# information to the user. In this exercise, we have to put it all together
# and add logic for handling guesses.

# Copy your code from Parts 1 and 2 into a new file as a starting point. Now 
# add the following features:

# Only let the user guess 6 times, and tell the user how many guesses they 
# have left.
# Keep track of the letters the user guessed. If the user guesses a letter 
# they already guessed, don’t penalize them - let them guess again.
# Optional additions:

# When the player wins or loses, let them start a new game.
# Rather than telling the user "You have 4 incorrect guesses left", display 
# some picture art for the Hangman. This is challenging - do the other parts 
# of the exercise first!
# Your solution will be a lot cleaner if you make use of functions to help 
# you!

import random

def user_word_init(len_word):
	i = 0
	user_word = []
	while i < len_word:
		user_word.append("_")
		i += 1
	return(user_word)

if __name__=="__main__":
	word_file = [line.strip() for line in open('30_sowpods.txt', 'r')]
	guess_word = random.choice(word_file)
	split_word = list(guess_word)
	len_split = len(split_word)
	user_word = user_word_init(len_split)
	user_trys = 6
	playing = True
	print(' '.join(user_word))
	print("Welcome to hangman")
	while playing:
		user_input = input("Guess your letter: ")
		user_trys -= 1
		x = -1
		for i in split_word:
			x += 1
			if user_input == i:
				user_word[x] = user_input	
		print(str(user_trys) + " guesses left")
		print(' '.join(user_word))
		if split_word == user_word:
						print ("Amazing!")
						break
		if user_trys == 0:
			print ("You lose!")
			play_again = input("Want to play again? (Yes) ")
			if play_again == "Yes":
				user_trys = 6
				user_word = user_word_init(len_split)
				playing == True
			else:
				playing == False
				break