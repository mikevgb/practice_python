# -*- coding: utf-8 -*-
# Take two lists, say for example these two:

#   a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#   b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

# and write a program that returns a list that contains only the elements that
# are common between the lists (without duplicates). Make sure your program works
# on two lists of different sizes.

# Extras:

# Randomly generate two lists to test this
# Write this in one line of Python (don’t worry if you can’t figure this out at
# this point - we’ll get to it soon)

import random

random_range_a = random.randint(1,50)
random_range_b = random.randint(1,50)
random_a = []
random_b = []
common = []

for i in range(0, random_range_a):
	n = random.randint(0, 100)
	random_a.append(n)

for i in range(0, random_range_b):
	n = random.randint(0, 100)
	random_b.append(n)

for number in random_a:
	if number in random_b:
		common.append(number)

clean_common = list(set(common))

print (clean_common)
