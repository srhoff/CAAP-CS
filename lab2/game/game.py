# imports multiple clases from the python library and some of our
# own modules.
from sys import exit
from random import randint
from map import Map
from leaderboard import Leaderboard
from scores import Score
from game_engine import Engine
import json

# global variables to keep track of score, player, and leaderboard
moves = 0
name = ""
leaderboard = Leaderboard()

# what happens when the game is over
# takes in a boolean parameter
# should update leaderboard, global variables, and print leaderboard
def game_over(won):
	global name
	global moves
	score = Score(name, moves)
	if won:
		print("*****************************************************************")
		print("Congratulations! You've WON!!!!!!!!!!!")
		leaderboard.update(score)
	else:
		print("*****************************************************************")
		print("GAME OVER")
	print ("\nGame Over.")
	name = ""
	moves = 0
	leaderboard.leaderboard_append()
	leaderboard.print_board()
	r_multiplier = 0

# initializes/updates global variables and introduces the game.
# starts the Map and the engine.
# ends the game if needed.
def play_game():
	while True:
		global name
		global moves
		print ("Welcome to my game! To quit enter :q at any time. Good luck!")
		name = input("\nLet's play. Enter your name. > ")
		if (name == ':q'):
			exit(1)
			#Difficulty---------------------------------------------
		multiplier = eval(input("Choose level of difficulty: \n[1] Easy (*1 score multiplier)\n[2] Medium(*.75 score multiplier)\n[3] Hard(*.5 score multiplier)\n >"))
		try:
			multiplier = int(multiplier)
		except:
			raise ValueError("Error: Please enter an integer 1-3")
		if not (multiplier < 4 or multiplier > 0):
			raise ValueError("Error: Incorrect level of difficulty")
		if multiplier == 1:
			lives = 3
			r_multiplier = 1
		if multiplier == 2:
			r_multiplier = .75
			lives = 2
		if multiplier == 3:
			r_multiplier = .5
			lives = 1
			#End of Difficulty Programming----------------------------------
		a_map = Map('den')
		a_game = Engine(a_map, lives)
		moves = a_game.play()
		moves *= r_multiplier
		game_over(a_game.won())
		break

play_game()
