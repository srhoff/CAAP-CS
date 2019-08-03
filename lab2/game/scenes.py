# imports random madule form library
from random import randint
from game_engine import Engine
# the base class for the scenes.
# Each scene has one variable name, and three functions: enter(), action(), and exit_scene().
# Read through the ones given, feel free to add more using the same template I've given you.
# Change, edit, or completely remove the scenes I gave you. Up to you.
class Scene(object):

	def enter(self):
		print ("This is the base scene class that's inherited by the other scenes, so it is not configured yet.")
		print ("Subclass it and implement enter(), action(), and exit_scene() for each scene.")
		exit(1)

	def exit_scene(self, outcome):
		return outcome
	#This is the beginning scene: leads to StraightPath
class Den(Scene):
	name = "den"

	def enter(self):
		print ("You are a dragon. Not gonna lie you're a pretty lazy dragon. That's the reason you built your den in the top of a dormant volcano. You just dropped in through the top and went to sleep, easy as taking money from... well anyone you're a dragon" )
		print ("Everything was perfect until one day the mountain begins to rumble. *CRACK* the summit collapses, rocks thundering down to bury you alive.")
		return self.action()

	def action(self):
		print ("You only have a split second to decide: ")
		choice = input("[1] Do you stay put?\n[2] Flee down into the mountain?\n > ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You die")
			return self.exit_scene('death')
		elif int(choice) == 2:
			print ("You flee down into the mountain")


			return self.exit_scene('straight_path')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome
	#This is the scene that communicates to the game that its done
class Finished(Scene):
	name = 'finished'
	#This leads to Springs
class StraightPath(Scene):

	name = "straight_path"

	def enter(self):
		print ("You come to a shrine. It is made of a dark stone, rounded at the top and embedded with a human skull. In each eye socket a ruby shines at you before going dun")
		return self.action()

	def action(self):
		print ("From here you would have two paths, if the left one had not been caved in years earlier. Using your heightened dragon senses you can tell that one cave is hotter while the other was decidedly cool")
		choice = input("[1] Turn Down the Hot Path\n >")
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
			print ("You head down the Hot Path")
			return self.exit_scene('springs')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game")
			return self.exit_scene(self.name)
			#Has not been Checked ##IDEA: MAYBE IF YOU WERE A LITTLE FASTER YOU COULDVE CAUGHT THEMM

	def exit_scene(self, outcome):
		return outcome
	#This is the first scene in the steam room
class Steam(Scene):
	name = 'steam'

	def enter(self):
		print ("You dive down through the hot spring. You swoop out of the falling water as you come through the ceiling of a new room. It immediately hits you that, if the hot spring was steamed up and hot then this must be enough to kill any normal life. Thankfully as a dragon you're insulated against the worst of the heat so you're fine. As you look around though your vision is obscured entirely by dense steam. Floating colors lay inside the steam, playing haunting light on the area. As you squint into the area you hear a faint rumbling: the mountain is still collapsing, and it is getting closer.")
		return self.action()

	def action(self):
		print("You can see a Brown, a Red, and a Yellow light in the steam. Which do you Follow?")
		choice = input("[1] Brown\n[2] Red\n[3] Purple\n > ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You blindly follow the brown light into the steam")
			return self.exit_scene('death')
		elif int(choice) == 2:
			print ("You blindly follow the red light into the steam")
			return self.exit_scene('steamA')
		elif int(choice) == 3:
			print ("You blindly follow the purple light into the steam")
			return self.exit_scene('death')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game")
			return self.exit_scene(self.name)
	def exit_scene(self, outcome):
		return outcome
	#First Decision: Steam
class SteamA(Scene):
	name = 'steamA'

	def enter(self):
		print ("The red light leads you somewhere else. Thankfully not into a horrible deathtrap, but the spirit has deserted you. Now you see an Orange light, a Turquoise light, and a Black light")
		return self.action()

	def action(self):
		print("Which do you Follow?")
		choice = input("[1] Orange\n[2] Turquoise\n[3] Black\n > ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You blindly follow the Orange light into the steam")
			return self.exit_scene('death')
		elif int(choice) == 2:
			print ("You blindly follow the Turquoise light into the steam")
			return self.exit_scene('death')
		elif int(choice) == 3:
			print ("You blindly follow the Black light into the steam")
			return self.exit_scene('steamAB')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game")
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome
	#Second Decision: Steam
class SteamAB(Scene):
	name = 'steamAB'

	def enter(self):
		print ("The black light leads you somewhere else. You don't know how you were able to see a black light, but oh well. The spirit has deserted you. Now you see a Green light, a Light Blue light, and an Aquamarine light")
		return self.action()

	def action(self):
		print("Which do you Follow?")
		choice = input("[1] Green\n[2] Light Blue\n[3] Aquamarine\n > ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You blindly follow the Green light into the steam")
			return self.exit_scene('steamABC')
		elif int(choice) == 2:
			print ("You blindly follow the Light Blue light into the steam")
			return self.exit_scene('death')
		elif int(choice) == 3:
			print ("You blindly follow the Aquamarine light into the steam")
			return self.exit_scene('death')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)
	def exit_scene(self, outcome):
		return outcome
	#Third Decision: Steam
class SteamABC(Scene):
	name = 'steamABC'

	def enter(self):
		print ("The Green light leads you somewhere else. Now there is only one light, emanating from a spirit hovering above the Steam vent. A Maroon Light. It seems to want you to jump down")
		return self.action()

	def action(self):
		print("Do you Follow?")
		choice = input("[1] Yes of course. Maroon is a sensible, inspiring color\n > ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)

		if int(choice) == 1:
			print ("You Confidently fall down the steam vent")
			return self.exit_scene('wet_escape')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)


	def exit_scene(self, outcome):
		return outcome
	#First scene in Springs room: Goes to Harold Inky and Stinky Dialogues
class Springs(Scene):
	name ='springs'

	def enter(self):
		print ("As you travel the cave, you begin to notice it becoming brighter, and you feel the humidity in the air. You spy an opening ahead preceded by two torch-holders bearing luminescent orange stones. Entering, you are acosted by steam emanating from the bubbling pools filling this room. You can see what looks to be a doorway on the other side of the room. However, you are once again acosted, this time by the sight of 3 nearly naked one-eyed ogres chilling in a hot spring 5 feet apart. Unfortunately, they are directly in your way.")
		print ("Harold the Ogre: Hello! Haven't seen you around these parts before. My name is Harold, and these are my bros Inky and Stinky.")
		print ("Looking on either side of the red ogre you see a similar looking black ogre (who you assume must be Inky) and a slightly smaller green Ogre who, judging by the smell of his clothing which lay not far off, must be Stinky")
		print ("Harold: Come, take a soak with us monseuir Reptile")
		print ("Inky: Talk to Me!")
		print ("Stinky: No, talk to me first! (He smells really bad)")
		return self.action()

	def action(self):
		print("What do you say?")
		choice = input("[1] Sure Harold\n[2] Sure Inky, what do you want to talk about\n[3] errrr... okay Stinky?\n > ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
			print("That's not an int!")
			return self.exit_scene(self.name)
		if int(choice) == 1:
			print ("*you sit down in the hot springs*")
			return self.exit_scene('springsA')
		elif int(choice) == 2:
			print ("*you sit down in the hot springs*")
			return self.exit_scene('springsB')
		elif int(choice) == 3:
			print ("*you sit down in the hot springs, careful to stay just far enough away from the grossness infecting the pool immediately next to Stinky*?")
			return self.exit_scene('springsC')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game")
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome
	#Begin Harold Dialogues
class SpringsA(Scene):
	name ='springs'

	def enter(self):
		print ("Harold: Ah, now you, being a dragon, are clearly well versed on the topic of Thermodynamics are you not? It's been so dull talking to these imbeciles for so long\n Inky: Hey!\n Stinky: Thats valid I'm gross\n *You hear rumbling*")
		return self.action()

	def action(self):
		print("What do you say?")
		choice = input("[1]  [Lie] Of Course, ThermoDynamics is a Passion of Mine \n[2]  [Lie] I know some thermodynamics but I learned it so long ago I don't know nearly as much as I should \n[3]  Nope \n > ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
				print("That's not an int!")
				return self.exit_scene(self.name)
		if int(choice) == 1:
			print ("")
			return self.exit_scene('springsAA')
		elif int(choice) == 2:
			print ("")
			return self.exit_scene('springsAA')
		elif int(choice) == 3:
			print ("")
			return self.exit_scene('springsAC')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome
	#Tell the Truth to Harold
class SpringsAC(Scene):
	name ='springsAC'

	def enter(self):
		print ("Harold looks crestfallen.\n Harold: I thought as a dragon I might finally have someone who could share my love of thermodynamics...")
		return self.action()

	def action(self):
		print("What do you say?")
		choice = input("[1]  Thermodynamics is shit anyway\n[2]  [Lie] I could learn to love it \n[3]  How do I leave? \n > ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
				print("That's not an int!")
				return self.exit_scene(self.name)
		if int(choice) == 1:
			print ("Harold: You are an asshole. That is my true passion. You die here")
			return self.exit_scene('death')
		elif int(choice) == 2:
			print ("Harold: FAKE FAN")
			return self.exit_scene('death')
		elif int(choice) == 3:
			print ("Harold: You will not sully the reputation of THERMODYNAMICS and WALK AWAY")
			return self.exit_scene('death')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)

	def exit_scene(self, outcome):
		return outcome
	#Lie to Harold: Leads to AAC
class SpringsAA(Scene):
	name ='springsAA'

	def enter(self):
		print ("Harold: Oh now I'm truly excited. Tell me, what is your knowledge of the second law? *the rumbling is even closer now*")
		return self.action()

	def action(self):
		print("What do you say?")
		choice = input("[1]  [Lie] The second law is child's play my friend, have you been introduced to the 123rd?\n[2]  [Lie] That is Obviously when something gets slower over time.. right? \n[3]  Well, uh, i kinda asssumed we wouldn't be talking about it anymore so I lied earlier\n > ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
				print("That's not an int!")
				return self.exit_scene(self.name)
		if int(choice) == 1:
			print ("")
			return self.exit_scene('springsAAA')
		elif int(choice) == 2:
			print ("")
			return self.exit_scene('springsAAA')
		elif int(choice) == 3:
			print ("")
			return self.exit_scene('springsAAC')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)
	def exit_scene(self, outcome):
		return outcome
	#Keep lying to Harold
class SpringsAAA(Scene):
	name ='springsAAA'

	def enter(self):
		print ("Harold: Ah yes, thats exactly it. Entropy, truly a concept worthy of an ogre of myself. I tend to blend my studies, so answer me this: is society in entropy?")
		return self.action()

	def action(self):
		print("What do you say?")
		choice = input("[1] No, of course society is not in entropy. Well just the other day humans brought a new invention to their village. Blasting Powder I think it was called.\n[2] Yes, every society decays. I believe that it decays consistently and is counteracted by great people or inventions.\n > ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
				print("That's not an int!")
				return self.exit_scene(self.name)
		if int(choice) == 1:
			print ("You got too caught up in your conversation and ignored the sounds of the cave-in. You are crushed beneath the water of the hot springs")
			return self.exit_scene('death')
		elif int(choice) == 2:
			print ("You got too caught up in your conversation and ignored the sounds of the cave-in. You are crushed beneath the water of the hot springs")
			return self.exit_scene('death')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)
	def exit_scene(self, outcome):
		return outcome
	#Cop out of lying to Harold
class SpringsAAC(Scene):
		name ='springsAAC'

		def enter(self):
			print ("Harold: Why would you lie to me?")
			return self.action()

		def action(self):
			print("What do you say?")
			choice = input("[1]  [Lie] I didn't want to hurt your feelings! I love you! But to love you I must leave you, how do you leave this hot spring? \n[2]  I Don't know man I live life as a game! \n[3] Just tell me how to leave man \n > ")
			if choice == ':q':
				return self.exit_scene(choice)
			try:
				choice = int(choice)
			except ValueError:
					print("That's not an int!")
					return self.exit_scene(self.name)
			if int(choice) == 1:
				print ("Harold: I love you too *you embrace and have your first kiss*. You're too deep in your lies and are cushed beneath the water of the hot springs")
				return self.exit_scene('death')
			elif int(choice) == 2:
				print ("Harold: You are a fake fan! I can't believe I almost fell for you! *You begin to cry, overcome with emotion*. You are crushed beneath the water of the hot spring")
				return self.exit_scene('death')
			elif int(choice) == 3:
				print ("Harold: So callous... I can't believe you would hurt me this way. Go! There is a secret exit in the bottom of the next hot spring. You leap through, tired of Harold's pedantic mutterings")
				return self.exit_scene('steam')
			else:
				print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
				return self.exit_scene(self.name)
		def exit_scene(self, outcome):
			return outcome
	#Inky Dialogue Begins
	##Both yes and no ARE meant to go to the game
class SpringsB(Scene):
	name ='springsB'

	def enter(self):
		print("Inky: Yay! Do you want to play a game?\n *You hear rumbling*")
		return self.action()

	def action(self):
		print("What do you say?")
		choice = input("[1] Yes\n[2] No\n[3] Maybe so\n > ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
				print("That's not an int!")
				return self.exit_scene(self.name)
		if int(choice) == 1:
			print ("")
			return self.exit_scene('springsBA')
		elif int(choice) == 2:
			print ("")
			return self.exit_scene('springsBA')
		elif int(choice) == 3:
			print ("I DO NOT TOLERATE INDECISIVENESS")
			return self.exit_scene('death')
		else:
			print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
			return self.exit_scene(self.name)
	def exit_scene(self, outcome):
		return outcome
	#Stinky Dialogue Begins
class SpringsC(Scene):
		name ='springsC'

		def enter(self):
			print("*The water around Stinky is revolting*\n Stinky: Heyyyyyy hoooowwwwss it hannnnggggin")
			return self.action()

		def action(self):
			print("What do you say?")
			choice = input("[1] heeyyyy i'm good...\n[2] PLEASE LET ME LEAVE\n[3] *vomits*\n > ")
			if choice == ':q':
				return self.exit_scene(choice)
			try:
				choice = int(choice)
			except ValueError:
					print("That's not an int!")
					return self.exit_scene(self.name)
			if int(choice) == 1:
				print ("")
				return self.exit_scene('springsCA')
			elif int(choice) == 2:
				print ("Stinky: Yeahhhh mannnn just go through the bottom of the hot spring behind meeeee.\n You FLEE through the hot spring")
				return self.exit_scene('steam')
			elif int(choice) == 3:
				print ("Your vomit reacts violently to the vile Stinky Water. Not even dragon's scales could protect you")
				return self.exit_scene('death')
		def exit_scene(self, outcome):
			return outcome
	#Stinky Awkward Death Scene
class SpringsCA(Scene):
	name ='springsCA'

	def enter(self):
		print("Stinky: Niceeeeee\n*\n*\nThis is extremely awkward")
		return self.action()

	def action(self):
		print("What do you do?")
		choice = input("[1] Die of Awkwardness> ")
		if choice == ':q':
			return self.exit_scene(choice)
		try:
			choice = int(choice)
		except ValueError:
				print("That's not an int!")
				return self.exit_scene(self.name)
		if int(choice) == 1:
			print ("")
			return self.exit_scene('death')
	def exit_scene(self, outcome):
		return outcome
	#You Won Inky's Game
class SpringsBAD(Scene):
		name ='springsB'

		def enter(self):
			print("Inky: Congratualtions! You get one wish! *the rumbling is much closer now*")
			return self.action()

		def action(self):
			print("What do you say?")
			choice = input("[1] Infinite Wealth\n[2] Infinite Lives\n[3] WHERE IS THE EXIT\n > ")
			if choice == ':q':
				return self.exit_scene(choice)
			try:
				choice = int(choice)
			except ValueError:
					print("That's not an int!")
					return self.exit_scene(self.name)
			if int(choice) == 1:
				print ("Before he can grant your wish, if he could've to begin with, you are crushed beneath the water of the hot spring")
				return self.exit_scene('death')
			elif int(choice) == 2:
				print ("Before he can grant your wish, if he could've to begin with, you are crushed beneath the water of the hot spring")
				return self.exit_scene('death')
			elif int(choice) == 3:
				print ("Inky: There is a secret exit under the next Hot Spring.\n You leap through the water.")
				return self.exit_scene('steam')
			else:
				print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
				return self.exit_scene(self.name)
		def exit_scene(self, outcome):
			return outcome
	#Second Decision in Escape Room
class WetEscapeA(Scene):
	name = 'wet_escapeA'
	def enter(self):
		print("You come to a second set of caves. One is filled with menacing stalagmites, the other with equally menacing stalactites. You must choose the one that would be safest for you, and fast. The cave is still collapsing behind you")
		return self.action()

	def action(self):
				print ("You only have a split second to decide: Which way do you Turn?")
				choice = input("[1] Stalagmite\n[2] Stalactite\n >  ")
				if choice == ':q':
					return self.exit_scene(choice)
				try:
					choice = int(choice)
				except ValueError:
					print("That's not an int!")
					return self.exit_scene(self.name)
				if int(choice) == 1:
					print ("You choose the stalagmite path. Thankfully you weren't always such a lazy dragon. In the 5th grade at dragon school you learned that stalactites hang from the ceiling, and so would be much more dangerous to a flying dragon")
					return self.exit_scene('wet_escapeAB')
				elif int(choice) == 2:
					print ("You take a chance on the stalactites. As you try to navigate the cave your wings are ripped to shreds by the stalactites hanging from the ceiling")
					return self.exit_scene('death')
				else:
					print ("DOES NOT COMPUTE! Choose an option or type :q to end game")
					return self.exit_scene(self.name)
	def exit_scene(self, outcome):
		return outcome
	#Final Decision: Escape Room
class WetEscapeAB(Scene):
	name = 'wet_escapeAB'
	def enter(self):
		print("Finally, the end is in sight! You can see the opening of the cave, the light beyond, the trees and the birds and the bees. But then you begin to feel an intense sense of apathy. Is this even important? Why am I here? Should I really be heading out there? I don't have a home anymore. I have no money, no friends, and no family. I will be completely alone, and nobody would miss me if I vanished under this mountain. Everyone I've met so far is dead, crushed under tons of rubble. What life is out there for me other than one of wandering and lonliness for all eternity? I could just lay down here, give up, and sleep forever.")
		return self.action()
	def action(self):
				print ("What do you decide to do?")
				choice = input("[1] Accept Mortality\n[2] Escape\n > ")
				if choice == ':q':
					return self.exit_scene(choice)
				try:
					choice = int(choice)
				except ValueError:
					print("That's not an int!")
					return self.exit_scene(self.name)

				if int(choice) == 1:
					print ("You lay down in the water, blocking the stream that flows out of the mountain and enriches the countryside. You are crushed to death. Had you not done this the water would have still found its way out and continued to spread life and vitality through the surrounding forests and down through settlements that stretched from here to the ocean. Now your decision will be felt by untold numbers of people who can no longer grow crops or feed their families. By plants and animals that relied on the consistent water that preserved this natural ecosystem. You should be ashamed.")
					return self.exit_scene('death')
				elif int(choice) == 2:
					print ("You snap out of your doldrum, fighting your way through the collapsing cave and out into open air.")
					return self.exit_scene('outside')
				else:
					print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
					return self.exit_scene(self.name)
	def exit_scene(self, outcome):
		return outcome
	#Kill the Humans
class Outside(Scene):
	name = 'outside'
	def enter(self):
		print("Sunlight. Trees. Birds and Bees. The world is open to you, the river rushing out from the collapsed cave enriching the lives of untold number of plants and animals on it's quest to the sea. You take a new perspective on life, this near death experience has taught you the value of your time here on this planet. No more will you be a lazy dragon! Dimly, you hear cheers from high above you. Soaring up to the mountain top, you see a group of about 500 men and the ruins that once were the top of your volcano hideout. The men look up at you, all gaity and laughter fallen from their faces. The obvious blasting charges they set make it clear that these men intentionally ruined your home. All the resources were deep in the mountain anyways, the men's motives were clear: They wanted you dead. Unfortunately for them they failed. You sneer at these pests. You'll enjoy what comes next")
		return self.action()

	def action(self):
				print ("What Do You Choose?")
				choice = input("[1] Burn them all alive\n[2] Capture most and pack them in a snack container you can use on your travels\n[3] Fly to their settlement and raze it to the ground, leaving them as the only survivors\n >")
				if choice == ':q':
					return self.exit_scene(choice)
				try:
					choice = int(choice)
				except ValueError:
					print("That's not an int!")
					return self.exit_scene(self.name)

				if int(choice) == 1:
					print ("You Burn them to a crisp, then fly off into the sunset")
					return self.exit_scene('finished')
				elif int(choice) == 2:
					print ("You pack many of them into a carry-on, and snack on them as you fly off into the sunset")
					return self.exit_scene('finished')
				elif int(choice) == 3:
					print ("You kill all of their families! You then fly off into the sunset.")
					return self.exit_scene('finished')
				else:
					print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
					return self.exit_scene(self.name)
	def exit_scene(self, outcome):
		return outcome
	#First Decision: Escape Room
class WetEscape(Scene):
	name = 'wet_escapeA'
	def enter(self):
		print("Diving once more, you swoop through the steam rising through the vent as the Steam Room crumbles behind you. Once out of the vent you have to pull up quickly for you're falling straight for the ground. You swoop ahead, looking at the treacherous river-cave system ahead of you. There is light at the far end, but as your hopes begin to rise rocks crash through the steam vent and the cave begins to groan and crack behind you. You steel yourself, and fly ahead as fast as you can. You come to a break in the cave and can only choose one way to go, the collapsing cave will make backtracking impossible. You hear frogs and crickets down one path, but down the second path you hear no animals but it looks brighter")
		return self.action()

	def action(self):
				print ("You only have a split second to decide: Which way do you Turn?")
				choice = input("[1] Animal Path\n[2] Light Path\n >")
				if choice == ':q':
					return self.exit_scene(choice)
				try:
					choice = int(choice)
				except ValueError:
					print("That's not an int!")
					return self.exit_scene(self.name)

				if int(choice) == 1:
					print ("You choose the left path, hoping beyond hope that the presence of animals means that they must have found a way in from that direction. The cave eventually becomes brighter") #before you are faced with a new choice of path: On the left the cave is filled with stalagmites, on the right stalagtites. You must choose the way that would be safest for you.")
					return self.exit_scene('wet_escapeA')
				elif int(choice) == 2:
					print ("You take a chance on the lighter side. As you move further and further down the light gets brighter, but you begin to have a hard time breathing. Too late you realize that this area must be filled with noxious fumes, and you know you must persevere or die. You come the end of the tunnel which was filled with lava, the source of the light you had seen. The cave collapses behind you, not quite crushing your little araa. It is a slow process, but eventually your tortured breathing slows and your heart stops.")
					return self.exit_scene('death')
				else:
					print ("DOES NOT COMPUTE! Choose an option or type :q to end game") # raise ValueError ('todo')
					return self.exit_scene(self.name)
	def exit_scene(self, outcome):
		return outcome
	#Inky's Game
class SpringsBA(Scene):
	name ='springsBA'

	def enter(self):
		print("*Inky puts three hands behind his back*\n Inky: How many hands am I holding up?")
		return self.action()

	def action(self):
		choice = 0
		while not choice == 4:
			print("What do you say?")
			choice = input("[1] 0\n[2] 1\n[3] 2\n[4] 3\n[5] 4\n > ")
			if choice == ':q':
				return self.exit_scene(choice)
			try:
				choice = int(choice)
			except ValueError:
				print("That's not an int!")
				return self.exit_scene(self.name)
			if int(choice) == 1:
				print ("Wrong!")
				return self.exit_scene('death')
			elif int(choice) == 2:
				print ("Wrong!")
				return self.exit_scene('death')
			elif int(choice) == 3:
				print ("Wrong!")
				return self.exit_scene('death')
			elif int(choice) == 4:
				return self.exit_scene('springsBAD')
			elif int(choice) == 5:
				print ("Wrong!")
				return self.exit_scene('death')
			else:
				print ("DOES NOT COMPUTE! Choose an option or type :q to end game")
				return self.exit_scene(self.name)
	def exit_scene(self, outcome):
		return outcome
