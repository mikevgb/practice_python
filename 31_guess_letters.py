# -*- coding: utf-8 -*-
# Let’s continue building Hangman. In the game of Hangman, a clue word is given 
# by the program that the player has to guess, letter by letter. The player guesses one letter at a time until the entire word has been guessed. (In the actual game, the player can only guess 6 letters incorrectly before losing).

# Let’s say the word the player has to guess is “EVAPORATE”. For this exercise,
# write the logic that asks a player to guess a letter and displays letters 
# in the clue word that were guessed correctly. For now, let the player guess
# an infinite number of times until they get the entire word. As a bonus, keep
# track of the letters the player guessed and display a different message if
# the player tries to guess that letter again. Remember to stop the game 
# when all the letters have been guessed correctly! Don’t worry about 
# choosing a word randomly or keeping track of the number of guesses the 
# player has remaining - we will deal with those in a future exercise.

# An example interaction can look like this:

# >>> Welcome to Hangman!
# _ _ _ _ _ _ _ _ _
# >>> Guess your letter: S
# Incorrect!
# >>> Guess your letter: E
# E _ _ _ _ _ _ _ E
# ...
# And so on, until the player gets the word.



# def letter_guess(guess_word)

def user_word_init(len_word):
	i = 0
	user_word = []
	while i < len_word:
		user_word.append("_")
		i += 1
	return(user_word)


if __name__=="__main__":
	guess_word = "EVAPORATE"
	split_word = list(guess_word)
	len_split = len(split_word)
	user_word = user_word_init(len_split)
	print(' '.join(user_word))
	print("Welcome to hangman")
	while True:
		user_input = raw_input("Guess your letter: ")
		x = -1
		for i in split_word:
			x += 1
			if user_input == i:
				user_word[x] = user_input
		print(' '.join(user_word))
		if split_word == user_word:
						print ("Amazing!")
						break