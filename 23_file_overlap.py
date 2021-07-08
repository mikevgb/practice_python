# -*- coding: utf-8 -*-
# Given two .txt files that have lists of numbers in them, find the numbers
# that are overlapping. One .txt file has a list of all prime numbers under
# 1000, and the other .txt file has a list of happy numbers up to 1000.

# (If you forgot, prime numbers are numbers that can’t be divided by any other
# number. And yes, happy numbers are a real thing in mathematics - you can 
# look it up on Wikipedia. The explanation is easier with an example, which
# I will describe below.)

primes = [line.strip() for line in open('23_primes.txt', 'r')]
happy = [line.strip() for line in open('23_happy.txt', 'r')]

joined = primes + happy
final_list = []
for i in joined:
	if i in final_list:
		final_list.append(i)
print(final_list)
