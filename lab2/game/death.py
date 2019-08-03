# importing random int maker module
from random import randint

# class defines what happens when a player dies.
# in this case, it has a list of phrases to be displayed
# randomly, and returns the string 'died' to let the engine know.
class Death(object):
	quips = ["You died.  You kinda suck at this.",
			"Maroon is the new Crimson... or shall I say, your blood is drying on the rocks\nfrom a crimson to a deep maroon.",
			"Wow",
			"Maybe if you got out more you might have.. you know.. got out",
			"You don't belong at UChicago. Don't you wish you'd gone to NorthWestern?",
			"CAAP? More like Can't Always Achieve Perfection"
			]
	#PRINT THE QUIPS
	def enter(self):
		print (Death.quips[randint(0, len(self.quips)- 1)])
		return 'died'
