import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from environment import NOT_HELD

class Player:
	'Base class for player'

	def __init__(self, name):
		if name == NOT_HELD:
			raise ValueError('Reserved namespace')
		else:
			self.name = name
		self.hand = []