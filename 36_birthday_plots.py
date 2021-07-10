#  -*- coding: utf-8 -*-

# In the previous exercise we counted how many birthdays there are in each month 
# in our dictionary of birthdays.

# In this exercise, use the bokeh Python library to plot a histogram of which 
# months the scientists have birthdays in! Because it would take a long time for
# you to input the months of various scientists, you can use my scientist 
# birthday JSON file. Just parse out the months (if you don’t know how, I 
# suggest looking at the previous exercise or its solution) and draw your 
# histogram.

# need to import at least 3 things to make your
# bokeh plots work
from bokeh.plotting import figure, show, output_file
import json
import datetime
import collections
import re

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

# print (collections.Counter(letter_month))
typeVariable = type(letter_month)
print('comparison',typeVariable == list)

pre_plot = [collections.Counter(letter_month)]

# pre_plot = re.findall(r'([+-]?\d+(?:\.\d+)?(?:[eE][+-]\d+)?)', pre_plot)
print (pre_plot)

# typeVariable = type(pre_plot)
# print('comparison',typeVariable == list)


# output_file("36_plot.html")
# x_categories = ["a", "b", "c", "d", "e"]
# x = ["a", "d", "e"]
# y = [4, 5, 6]

# p = figure(x_range=x_categories)
# p.vbar(x=x, top=y, width=0.5)

# show(p)