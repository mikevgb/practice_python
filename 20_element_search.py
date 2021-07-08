# Write a function that takes an ordered list of numbers (a list where the
# elements are in order from smallest to largest) and another number.
# The function decides whether or not the given number is inside the list
# and returns (then prints) an appropriate boolean.

# Extras:

# Use binary search.

num_list = [0, 1, 2, 3, 4]

def search_num(num_list, find_num):
	for i in num_list:
		if i == find_num:
			return True
	return False

print(search_num(num_list, 4))



