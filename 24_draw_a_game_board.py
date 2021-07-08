#  -*- coding: utf-8 -*-
# This exercise is Part 1 of 4 of the Tic Tac Toe exercise series. The other 
# exercises are: Part 2, Part 3, and Part 4.

# Time for some fake graphics! Let’s say we want to draw game boards that 
# look like this:

#  --- --- --- 
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- ---  
# |   |   |   | 
#  --- --- --- 
# This one is 3x3 (like in tic tac toe). Obviously, they come in many other 
# sizes (8x8 for chess, 19x19 for Go, and many more).

# Ask the user what size game board they want to draw, and draw it for them
# to the screen using Python’s print statement.

# Remember that in Python 3, printing to the screen is accomplished by

#   print("Thing to show on screen")

input_size = int(raw_input("Please, enter the size of the board: "))

def line1 (input_size):
	return (" ---" * input_size + " \n")

def line2 (input_size):
	return ("|   " * input_size + "|\n")

def g_board (input_size):
	board = ""
	for x in range(input_size):
		board += line1(input_size)
		board += line2(input_size)
	board += line1(input_size)
	return board

print(g_board(input_size))
