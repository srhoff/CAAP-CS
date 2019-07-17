# imports random madule form library
from random import randint

# the base class for the scenes.
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene().
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):

	def enter(self):
		print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
		print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
		exit(1)

class den(Scene):

	name = "den"

	def enter(self):
		print ("You are a dragon. Not gonna lie you're a pretty lazy dragon. That's the reason you built your den in the top of a dormant volcano. You just dropped in through the top and went to sleep, easy as taking money from... well anyone you're a dragon" )
		print ("Everything was perfect until one day the mountain begins to rumble. *CRACK* the summit collapses, rocks thundering down to bury you alive."
		raise ValueError ('todo')
		return self.action()


	def action(self):
		print ("You only have a split second to decide: do you stay put, flee down into the mountain, or do you flee down the straight cave?")
		choice = input("> ")
		if choice == ':q':
			return self.exit_scene(choice)
		# this is some exception handling, you don't need to worry about it,
		# just accept that it works and keeps the program from falling apart.
		try:
		   choice = int(choice)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You die")
			return self.exit_scene('death')
		elif int(choice) == 2:
			print ("You flee down the Straight Path")
			return self.exit_scene('straight_path')
		elif int(choice) == 3:
			print ("You flee down into the mountain")
			return self.exit_scene('down_path')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome

class straight_path(Scene):

	name = "Straight Path Checkpoint"

	def enter(self):
		print ("You come to a shrine. It is made of a dark stone, rounded at the top and embedded with a human skull. In each eye socket a ruby shines at you before going dun")
		return self.action()

	print ("From here you have two paths. Using your heighted dragon senses you can tell that one cave is hotter while the other is decidedly cool")
	choice = input("> ")
	if choice == ':q':
		return self.exit_scene(choice)
	# this is some exception handling, you don't need to worry about it,
	# just accept that it works and keeps the program from falling apart.
	try:
	   choice = int(choice)
	except ValueError:
	   print("That's not an int!")
	   return self.exit_scene(self.name)

	if int(choice) == 1:
		print ("You head down the Hot Path ")
		return self.exit_scene('springs')
	elif int(choice) == 2:
		print ("You flee down the Cool Path")
		return self.exit_scene('mushroom')
	else:
		print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
		return self.exit_scene(self.name)

class springs(Scene):

	name ='the_bridge'

	def enter(self):
		raise ValueError ('todo')

	def action(self):
		raise ValueError ('todo')

	def exit_scene(self, outcome):
		raise ValueError ('todo')

class EscapePod(Scene):

	name = 'escape_pod'

	def enter(self):
		raise ValueError ('todo')


	def action(self):
		print ("There's 5 pods, which one do you take?")
		good_pod = randint(1,5)
		guess = input("[pod #]> ")

		if guess == ':q':
			return self.exit_scene(guess)
		try:
		   guess = int(guess)
		except ValueError:
		   print("That's not an int!")
		   return self.exit_scene(self.name)

		if int(guess) != good_pod:
			print ("You jump into pod %s and hit the eject button."% guess)
			raise ValueError ('todo')
			return self.exit_scene('death')
		else:
			print ("You jump into pod %s and hit the eject button."% guess)
			raise ValueError ('todo')
			return self.exit_scene('finished')

	def exit_scene(self, outcome):
		raise ValueError ('todo')
