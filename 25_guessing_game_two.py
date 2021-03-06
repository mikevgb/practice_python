#  -*- coding: utf-8 -*-
# In a previous exercise, we’ve written a program that “knows” a number and asks
# a user to guess it.

# This time, we’re going to do exactly the opposite. You, the user, will have in
# your head a number between 0 and 100. The program will guess a number, and you,
# the user, will say whether it is too high, too low, or your number.

# At the end of this exchange, your program should print out how many guesses it
# took to get your number.

# As the writer of this program, you will have to choose how your program will
# strategically guess. A naive strategy can be to simply start the guessing at 1,
# and keep going (2, 3, 4, etc.) until you hit the number. But that’s not an
# optimal guessing strategy. An alternate strategy might be to guess 50 (right
# in the middle of the range), and then increase / decrease by 1 as needed. 
# After you’ve written the program, try to find the optimal strategy! 
# (We’ll talk about what is the optimal one next week with the solution.)

def loop(original_num, user_input):
	if user_input == "high":
		sliced_num = original_num * 0.5
		return sliced_num
	if user_input == "low":
		sliced_num = original_num * 1.5
		return sliced_num


if __name__=="__main__":
	print ("Please, think of a number between 0 and 100")
	original_num = 50
	try_counter = 0
	while True:
		try_counter += 1
		user_input = str(input("Is your number " + str(round(original_num)) + "? answer low, high, or yes > "))
		original_num = loop(original_num, user_input)
		if user_input == "yes":
			print("hurray!")
			print(">ONLY< " + str(try_counter) + " trys!")
			break
