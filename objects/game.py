import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from random import shuffle
from . import card, team, player
from environment import HEARTS, DIAMONDS, SPADES, CLUBS, A, K, Q, J, TEN, NINE, SUITS, SYMBOLS

class Game:
	'Base class for a game'

	def __init__(self, team1, team2):
		self.team1 = team1
		self.team2 = team2
		self.deck = self.generateDeck()
		self.trump = ''
		self.faceup = None # faceup card to help determine trump for the round
		self.played = [] # list of cards played in a specific round

	# method to initialize a deck for the game
	def generateDeck(self):
		
		deck = []

		for suit in SUITS:
			for symbol in SYMBOLS:
				deck.append(card.Card(suit, symbol))

		return deck

	# method to start a round of Euchre
	def startRound(self):
		self.deal()
		self.faceup = self.deck[20]

	# method to evaluate who wins a hand
	# method returns the card which wins
	def evaluateHand(self):
		winning = None
		suitLed = None
		for card in self.played:
			if not winning:
				winning = card # first card played is by default winning
				suitLed = card.suit
			else:
				winning = self.evaluateCards(winning, card, suitLed)

		return winning

	# method to evaluate which card beats the other
	# method returns the card which wins
	# expects arguments in the following form,
	#    card1, card2 as instances of Card
	#    suitLed as one of [CLUBS, HEARTS, DIAMONDS, SPADES]
	def evaluateCards(self, card1, card2, suitLed):
		if self.isTrump(card1):
			if self.isTrump(card2):
				return self.evaluateTrump(card1, card2)
			else:
				return card1
		else:
			if self.isTrump(card2):
				return card2
			else:
				if card1.suit == suitLed:
					if card2.suit == suitLed:
						return self.evaluateNotTrump(card1, card2)
					else:
						return card1
				else:
					if card2.suit == suitLed:
						return card2
					else:
						# program is assumed to never compare in this situation, as neither card would
						# be winning
						raise ValueError('Cannot evaluate two non-trump cards which do not follow suit')

	# method to evaluate which of two same suit, non-trump cards win
	# method returns the card which wins
	# expects arguments (card1, card2)
	def evaluateNotTrump(self, card1, card2):
		card1Position = SYMBOLS.index(card1.symbol)
		card2Position = SYMBOLS.index(card2.symbol)
		if card1Position > card2Position:
			return card1
		elif card1Position < card2Position:
			return card2
		else:
			raise ValueError('Cannot compare same card')

	# method to evaluate which of two same suit, trump cards wins
	# method returns the card which wins
	# expects arguments 
	# 	card1, card2 as instances of Card
	def evaluateTrump(self, card1, card2):
		if self.isLeftBower(card1):
			if self.isLeftBower(card2):
				raise ValueError('Cannot compare same card')
			else:
				if card2.symbol == J:
					return card2
				else:
					return card1
		else:
			if self.isLeftBower(card2):
				if card1.symbol == J:
					return card1
				else:
					return card2
			else:
				return self.evaluateNotTrump(card1, card2) # no special Jack rules apply

	# method to determine if a card is trump
	# method returns True if trump, False if not trump
	# expects arguments
	# 	card as an instance of Card
	def isTrump(self, card):
		if card.suit == self.trump:
			return True
		elif self.isLeftBower(card):
			return True
		else:
			return False

	# method to determine if a card is a 'left bower' (counts as a trump card)
	# method returns True if left bower, False if not
	# expects arguments
	# 	card as an instance of Card
	def isLeftBower(self, card):
		if card.symbol == J:
			if ((card.suit == SPADES and self.trump == CLUBS) or
					(card.suit == CLUBS and self.trump == SPADES) or
					(card.suit == DIAMONDS and self.trump == HEARTS) or
					(card.suit == HEARTS and self.trump == DIAMONDS)):
				return True
			else:
				return False
		else:
			return False


	# method to deal a hand for a round	
	def deal(self):
		shuffle(self.deck)
		self.team1.player1.hand = self.deck[0:5]
		self.team1.player2.hand = self.deck[5:10]
		self.team2.player1.hand = self.deck[10:15]
		self.team2.player2.hand = self.deck[15:20]


	# method to display scores of teams
	def displayScores(self):
		return "Team 1: ", self.team1.gameScore, ", Team 2: ", self.team2.gameScore
