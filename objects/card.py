class Card:
	'Base class for a card'

	def __init__(self, suit, symbol):
		self.suit = suit # one of ['Clubs', 'Hearts', 'Diamonds', 'Spades']
		self.symbol = symbol # one of ['9', '10', 'J', 'Q', 'K', 'A']