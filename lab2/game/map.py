# imports scenes and death for creation of the Map
import scenes as S
from death import Death

# the map is created by the dictionary of scenes. If you add another parameter,
# you can probably add your own custom maps (as long as they somehow lead to end)?
class Map(object):
	scenes = {'den' : S.Den(),
				'straight_path' : S.StraightPath(),
				'down_path' : S.DownPath(),
				'hot_path_start' : S.HotPathStart(),
				'cool_path_start' : S.CoolPathStart(),
				'dry_path_start' : S.DryPathStart(),
				'dank_path_start' : S.DankPathStart(),
				'moldy' : S.Moldy(),
				'spider' : S.Spider(),
				'mushroom' : S.Mushroom(),
				'springs' : S.Springs(),
				'skeleton' : S.Skeleton(),
				'steam' : S.Steam(),
				'dry_escape' : S.DryEscape(),
				'wet_escape' : S.WetEscape(),
				'checkpoint_wet' : S.CheckWet(),
				'checkpoint_dry' : S.CheckDry(),
				'outside' : S.Outside(),
				'death' : Death()
				# raise ValueError ('todo')
				}

	# initializes to a starting scene
	def __init__(self, start_scene):
		self.start_scene = start_scene

	# gets the specified scene from the scenes dictionary list.
	def next_scene(self, scene_name):
		return Map.scenes.get(scene_name)

	# gets the first scene of the map from the dictionary list
	def opening_scene(self):
		return self.next_scene(self.start_scene)
