# Implement a function that takes as input three variables, and returns the 
# largest of the three. Do this without using the Python max() function!

# The goal of this exercise is to think about some internals that Python 
# normally takes care of for us. All you need is some variables and if 
# statements!

user_input = raw_input(" Please enter the numbers: ")
a, b, c = user_input.split()

def check_values(a, b, c):
	if a > b and a > c:
		print(a + " is the biggest")
	if b > a and b > c:
		print(b + " is the biggest")
	if c > a and c > b:
		print(c + " is the biggest")

check_values(a, b, c)