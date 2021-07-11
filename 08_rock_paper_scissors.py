# -*- coding: utf-8 -*-
# Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using 
# input), compare them, print out a message of congratulations to the winner, 
# and ask if the players want to start a new game)

# Remember the rules:

# Rock beats scissors
# Scissors beats paper
# Paper beats rock

import os

player1 = input("Player 1, please enter your move: ")
player2 = input("Player 2, please enter your move: ")
move_list = ["rock", "scissors", "paper"]

if player1 in move_list and player2 in move_list:
	if player1 == str("rock") and player2 == str("scissors"):
		print("Player 1 wins ")
	if player1 == str("scissors") and player2 == str("rock"):
		print("Player 2 wins ")
	if player1 == str("scissors") and player2 == str("paper"):
		print("Player 1 wins ")
	if player1 == str("paper") and player2 == str("scissors"):
		print("Player 2 wins ")
	if player1 == str("paper") and player2 == str("rock"):
		print("Player 1 wins ")
	if player1 == str("rock") and player2 == str("paper"):
		print("Player 2 wins ")
else:
	print ("Bad input, please enter rock, scissors or paper")

restart = input("Want to play again?(y/n) ")
if restart == str("y"):
	os.system("python 08_rock_paper_scissors.py 1")

