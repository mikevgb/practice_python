# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.).
# You can (and should!) use your answer to Exercise 4 to help you. Take this 
# opportunity to practice using functions, described below.

def get_number(text):
	return int(raw_input(text))

num = get_number("Please, enter a number: ")
x = range(1, num)

flag = False

for elem in x:
	if (num % elem) == 0:
		flag = True

if flag:
	print(str(num) + " is not a prime")
else:
	print(str(num) + " is a prime")