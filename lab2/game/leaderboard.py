# imports the score class to be used in the leaderboard.
from scores import Score
import json

# leaderboard keeps track of top ten highest ranking players
class Leaderboard(object):
	size = 10
	board = []

	def __init__(self):
		self.load_leaderboard()

	# prints the leaderboard
	def print_board(self):
		print("LEADERBOARD\n")
		for i in range(self.size):
			score = self.board[i]
			playerscore = score.get_score()
			playername = score.get_name()
			print("Player: ", playername, "\tMoves:",playerscore)
	# writes the leaderboard to leaderboard_save.txt, saving the leaderboard permanently
	def leaderboard_append(self):
		leaderboard_dict = {}
		for i in range(self.size):
			score = self.board[i]
			playerscore = score.get_score()
			playername = score.get_name()
			leaderboard_dict[str(i)] = [playerscore, playername]
		with open('leaderboard_save.txt','w') as outfile:
			json.dump(leaderboard_dict,outfile)

	#Loads the permanent leaderboard from leaderboard_save.txt
	def load_leaderboard(self):
		with open('leaderboard_save.txt','r') as json_file:
			data = json.load(json_file)
			for i in range(len(data)):
				player_data = data[str(i)]
				name = player_data[1]
				moves = player_data[0]
				score = Score(name, moves)
				self.board.append(score)

	# checks if given score should be in the leaderboard
	def update(self, score):
<<<<<<< HEAD
		if score.get_score() < board[-1].get_score():
		 	self.insert(score)

	# inserts the score in the given position (assuming it's better or equal to the one in the given rank)
	# moving everything below down a rank
	def insert(self, score):
		if score.get_score() < board[i].get_score():
			 #board[-1].get_score() < score.get_score() < board[-10].get_score()
			board[i] += 1
=======
		playerscore = score.get_score()
		for i in range(self.size):
			if playerscore < self.board[-1].get_score():
				self.insert_score(score)
				self.board.pop(-1)
				return

	# inserts the score in the given position (assuming it's better or equal to the one in the given rank)
	# moving everything below down a rank
	def insert_score(self, score):
		for index in range(self.size):
			if score.get_score() < self.board[index].get_score():
				self.board.insert(index,score)
				return
# leaderboard = Leaderboard()
# leaderboard.print_board()
# test = Score("Spencer", 4)
# leaderboard.update(test)
# leaderboard.print_board()
>>>>>>> ec73058d965d9b699951a91e29dc4142a0597449
