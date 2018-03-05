import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from environment import HEARTS, DIAMONDS, SPADES, CLUBS, A, K, Q, J, TEN, NINE, SUITS, SYMBOLS, NOT_HELD

class Card:
	'Base class for a card'

	def __init__(self, suit, symbol, holder=None):
		self.suit = suit # one of ['Clubs', 'Hearts', 'Diamonds', 'Spades']
		self.symbol = symbol # one of ['9', '10', 'J', 'Q', 'K', 'A']
		if holder == NOT_HELD:
			raise ValueError('Reserved namespace')
		elif holder:
			self.holder = holder # should be an instance of player
		else:
			self.holder = NOT_HELD

	# method to determine if a card is a 'left bower' (counts as a trump card)
	# method returns True if left bower, False if not
	# expects arguments
	# 	card as an instance of Card
	def isLeftBower(self, trump):
		if self.symbol == J:
			if ((self.suit == SPADES and trump == CLUBS) or
					(self.suit == CLUBS and trump == SPADES) or
					(self.suit == DIAMONDS and trump == HEARTS) or
					(self.suit == HEARTS and trump == DIAMONDS)):
				return True
			else:
				return False
		else:
			return False

	# method to determine if a card is trump
	# method returns True if trump, False if not trump
	# expects arguments
	# 	card as an instance of Card
	def isTrump(self, trump):
		if self.suit == trump:
			return True
		elif self.isLeftBower(trump):
			return True
		else:
			return False