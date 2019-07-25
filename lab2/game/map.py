# imports scenes and death for creation of the Map
import scenes as S
from death import Death

# the map is created by the dictionary of scenes. If you add another parameter,
# you can probably add your own custom maps (as long as they somehow lead to end)?
class Map(object):
	scenes = {'den' : S.Den(),
				'straight_path' : S.StraightPath(),
				'springs' : S.Springs(),
				'springsA': S.SpringsA(),
				'springsAC' : S.SpringsAC(),
				'springsAA' : S.SpringsAA(),
				'springsAAA' : S.SpringsAAA(),
				'springsAAC' : S.SpringsAAC(),
				'springsB' : S.SpringsB(),
				'springsC' : S.SpringsC(),
				'springsCA' : S.SpringsCA(),
				'springsBAD' : S.SpringsBAD(),
				'springsBA' : S.SpringsBA(),
				'steamABC' : S.SteamABC(),
				'steam' : S.Steam(),
				'steamA' : S.SteamA(),
				'steamAB' : S.SteamAB(),
				'wet_escape' : S.WetEscape(),
				'outside' : S.Outside(),
				'death' : Death(),
				'wet_escapeA' : S.WetEscapeA(),
				'wet_escapeAB' : S.WetEscapeAB(),
				'finished' : S.Finished()
				}

	# initializes to a starting scene
	def __init__(self, start_scene):
		self.start_scene = start_scene

	# gets the specified scene from the scenes dictionary list.
	def next_scene(self, scene_name): ##I will refer to things as scene name in my house
		return self.scenes.get(scene_name)

	# gets the first scene of the map from the dictionary list
	def opening_scene(self):
		return self.next_scene(self.start_scene)
