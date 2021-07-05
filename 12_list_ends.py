# Write a program that takes a list of numbers (for example,

# a = [5, 10, 15, 20, 25]) 
 
# and makes a new list of only the first and last elements of the given list.
# For practice, write this code inside a function.

a = [5, 10, 15, 20, 25]

def make_new_list(list_elements):
	return list_elements[::len(list_elements)-1]

new = make_new_list(a)
print (new)