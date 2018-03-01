import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from environment import HEARTS, DIAMONDS, SPADES, CLUBS, A, K, Q, J, TEN, NINE, SUITS, SYMBOLS

class Card:
	'Base class for a card'

	def __init__(self, suit, symbol):
		self.suit = suit # one of ['Clubs', 'Hearts', 'Diamonds', 'Spades']
		self.symbol = symbol # one of ['9', '10', 'J', 'Q', 'K', 'A']