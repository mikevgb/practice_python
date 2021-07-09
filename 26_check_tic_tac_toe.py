#  -*- coding: utf-8 -*-
# This exercise is Part 2 of 4 of the Tic Tac Toe exercise series. The other 
# exercises are: Part 1, Part 3, and Part 4.

# As you may have guessed, we are trying to build up to a full tic-tac-toe 
# board. However, this is significantly more than half an hour of coding, 
# so we’re doing it in pieces.

# Today, we will simply focus on checking whether someone has WON a game 
# of Tic Tac Toe, not worrying about how the moves were made.

# If a game of Tic Tac Toe is represented as a list of lists, like so:

# game = 	[[1, 2, 0],
# 			[2, 1, 0],
# 			[2, 1, 1]]

# where a 0 means an empty square, a 1 means that player 1 put their token 
# in that space, and a 2 means that player 2 put their token in that space.

# Your task this week: given a 3 by 3 list of lists that represents a Tic Tac Toe
# game board, tell me whether anyone has won, and tell me which player won, if
# any. A Tic Tac Toe win is 3 in a row - either in a row, a column, or a 
# diagonal. Don’t worry about the case where TWO people have won - assume that
# in every board there will only be one winner.


def check_rows(game, player_num, row):
	x = 0
	for i in game[row]:
		if i == player_num:
			x += 1
	return x

def check_col(game, player_num, row, col):
	x = 0
	for i in game[row][col]:
		if i == player_num:
			x += 1
	return x

def loop_col(i, player_num, cols, rows, results_cols, win_value):
	while i <= 5:
		results_cols.append(check_cols(game, player_num, rows, cols))
		i += 1
		rows = 0
		if cols == 3:
			player_num += 1
			cols = 0
		if player_num > 2:
			print(results_cols)
			break

def loop_rows(i, player_num, rows, results_rows, win_value):
	while i <= 5:
		results_rows.append(check_rows(game, player_num, rows))
		i += 1
		rows += 1
		if rows == 3:
			player_num += 1
			rows = 0
		if player_num > 2:
			print(results_rows)
			break


if __name__=="__main__":
	rows = 0
	cols = 0
	i = 0
	player_num = 1
	results_cols = []
	results_rows = []
	win_value = 3

	game = [[1, 2, 0],
			[2, 1, 0],
			[1, 1, 1]]
	loop_rows(i, player_num, rows, results_rows, win_value)
	i = 0
	player_num = 1
	loop_col(i, player_num, cols, rows, results_cols, win_value)


00 01 02
10 11 12
20 21 22