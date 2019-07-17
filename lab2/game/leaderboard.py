# imports the score class to be used in the leaderboard.
from scores import Score

# leaderboard keeps track of top ten highest ranking players
class Leaderboard(object):
	size = 10
	board = []

	def __init__(self):
		for i in range(self.size):
			name = 'player' + str(i)
			moves = 0
			score = Score(name, moves)
			self.board.append(score)

	# prints the leaderboard
	def print_board(self):
		print("LEADERBOARD\n")
		print(*board, sep = "\n")

	# checks if given score should be in the leaderboard
	def update(self, score):
		if score.get_score() < board[-1].get_score():
		 	self.insert(score)

	# inserts the score in the given position (assuming it's better or equal to the one in the given rank)
	# moving everything below down a rank
	def insert(self, score):
		if score.get_score() < board[i].get_score():
			 #board[-1].get_score() < score.get_score() < board[-10].get_score()
			board[i] += 1
