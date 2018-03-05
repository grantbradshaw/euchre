import os, sys
import random
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from environment import HEARTS, DIAMONDS, SPADES, CLUBS, NOT_HELD, SUITS

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
	def play(self, trump, suitLed):
		if suitLed:
			playable = list(filter(lambda x: self.canPlay(x, trump, suitLed), self.hand))
			if playable:
				return self.selectCard(playable)
			else:
				return self.selectCard(self.hand)
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
		if card.isLeftBower(trump):
			if suitLed == trump:
				return True
			else:
				return False
		elif card.suit == suitLed:
			return True
		else:
			return False

	# method which returns a player's response for trump when card face up
	# method returns a Boolean
	# expects arguments
	# 	card is the card which is face up
	# 	table is a list of players in the order they play and can decide trump, dealer last
	def decideTrumpFaceUp(self, card, table):
		if list(filter(lambda x: x.suit == card.suit, self.hand)):
			return True
		else:
			return False

	# method which returns a player's response for trump when card face down
	# method returns a Boolean
	# expects arguments
	# 	card is the card which was face up
	# 	table is a list of players in the order they play and can decide trump, dealer last
	def decideTrumpFaceDown(self, card, table):
		return random.choice(list(filter(lambda x: x != card.suit, SUITS)))







