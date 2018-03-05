import os, sys
import random
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from environment import HEARTS, DIAMONDS, SPADES, CLUBS, NOT_HELD

class Player:
	'Base class for player'

	def __init__(self, name):
		if name == NOT_HELD:
			raise ValueError('Reserved namespace')
		else:
			self.name = name
		self.hand = []

	# method to select a card to play
	# method returns a valid card to play
	# expects arguments
	# 	suitLed should be one of SPADES, HEARTS, DIAMONDS, CLUBS or None if first card played	
	def play(self, suitLed):
		if suitLed:
			pass
		else:
			return self.selectCard(self.hand)

	# method which randomly selects a card to play and removes it from the player's hand
	# method returns the card which is played
	# expects arguments
	# 	list_of_Cards should be a list of card instances of at least length 1
	def selectCard(self, list_of_cards):
		if list_of_cards:
			to_play = random.choice(list_of_cards)
			self.hand.remove(to_play)
			return to_play
		else:
			raise ValueError('Cannot select a card from empty list')

	# method which returns whether a card is valid to play
	# method returns a Boolean
	# expects arguments
	# 	card as an instance of card
	# 	trump as one of SPADES, HEARTS, DIAMONDS, CLUBS
	# 	suitLed as one of SPADES, HEARTS, DIAMONDS, CLUBS
	def canPlay(self, card, trump, suitLed):
		pass


