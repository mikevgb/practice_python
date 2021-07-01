# Create a program that asks the user to enter their name and their age. Print
# out a message addressed to them that tells them the year that they will turn
# 100 years old.

# Extras:

# Add on to the previous program by asking the user for another number and
# printing out that many copies of the previous message. (Hint: order of 
# operations exists in Python)
# Print out that many copies of the previous message on separate lines. 
# (Hint: the string "\n is the same as pressing the ENTER button)

import time

i = 1
name = raw_input("Please, enter your name: ")
age = int(raw_input("Please, enter your age: "))
many = int(raw_input("How many times would you like to print? "))
year = int(time.strftime("%Y"))
left_to_100 = int(100 - age)
total_age = year + left_to_100

if many > 0:
	while i <= many:
		print ("Dear " + name + ", you will turn 100 years old in " + str(total_age))
		i += 1
