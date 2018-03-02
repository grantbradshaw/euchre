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
			self.holder = holder
		else:
			self.holder = NOT_HELD