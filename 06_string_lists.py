# -*- coding: utf-8 -*-
# Ask the user for a string and print out whether this string is a palindrome or
# not. (A palindrome is a string that reads the same forwards and backwards.)

string = raw_input("Please, enter a string, we will check if is a palindrome ")

if (string == string[::-1]):
	print("String is a palindrome")
else:
	print("String is not a palindrome")
