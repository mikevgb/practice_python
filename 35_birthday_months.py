#  -*- coding: utf-8 -*-
# In the previous exercise we saved information about famous scientists’ names
# and birthdays to disk. In this exercise, load that JSON file from disk, extract
# the months of all the birthdays, and count how many scientists have a birthday
# in each month.

# Your program should output something like:

# {
# 	"May": 3,
# 	"November": 2,
# 	"December": 1
# }
import json
import datetime

from collections import Counter

with open("35.json") as file_js:
	data = json.load(file_js)

print("--------------------------------")
for i in data['important_people']:
        print("Name: " + i['name'])
        print("Birthday: " + i['birthday'])
	print("--------------------------------")

#extract data from raw imported json
raw_birthday = []
for i in data['important_people']:
	raw_birthday.append(i['birthday'])

#parse the new list and get the months
x = 0
month_list = []
while x < len(raw_birthday):
	temp = raw_birthday[x]
	month_list.append(temp[3:5])
	x += 1

#translate this int months into text
letter_month = []
x = 0
while x < len(raw_birthday):
	temp = month_list[x]
	month = datetime.date(1900, int(temp), 1).strftime('%B')
	letter_month.append(month)
	x += 1

print Counter(letter_month)


