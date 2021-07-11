# Write a program (using functions!) that asks the user for a long string
# containing multiple words. Print back to the user the same string,
# except with the words in backwards order. For example, say I type the string:

# My name is Michele

# Then I would see the string:

# Michele is name My

# shown back to me.

input_string = input("Please, enter a long string: ")

def split_string(input_string):
	new_list = input_string.split( )
	return (new_list)

def reverse_list(splited_string):
	rev_list = splited_string[::-1]
	return (rev_list)

def join_string(reverse_string):
	joined = (" ".join(reverse_string))
	return (joined)

new_list = split_string(input_string)
rev_list = reverse_list(new_list)
print(join_string(rev_list))
