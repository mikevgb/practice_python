#  -*- coding: utf-8 -*-

# This exercise is Part 1 of 4 of the birthday data exercise series. The other
# exercises are: Part 2, Part 3, and Part 4.

# For this exercise, we will keep track of when our friend’s birthdays are, and
# be able to find that information based on their name. Create a dictionary
# (in your file) of names and birthdays. When you run your program it should
# ask the user to enter a name, and return the birthday of that person back
# to them. The interaction should look something like this:

# >>> Welcome to the birthday dictionary. We know the birthdays of:
# Albert Einstein
# Benjamin Franklin
# Ada Lovelace
# >>> Who's birthday do you want to look up?
# Benjamin Franklin
# >>> Benjamin Franklin's birthday is 01/17/1706.
# Happy coding!

birthdays = {
	"Albert Einstein": "01/02/1900",
	"Benjamin Franklin": "01/17/1706",
	"Ada Lovelace": "03/03/3333"
}

print("Welcome to the birthday dictionary. We know the birthdays of:")
print('\n'.join(birthdays.keys()))

user_input = input("Who's birthday do you want to look up? ")

for i in birthdays:
	if i == user_input:
		print(birthdays[user_input])