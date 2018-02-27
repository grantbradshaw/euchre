from . import card, team, player
from random import shuffle

class Game:
	'Base class for a game'

	def __init__(self, team1, team2):
		self.team1 = team1
		self.team2 = team2
		self.deck = self.generateDeck()
		self.trump = ''
		self.faceup = None

	# method to initialize a deck for the game
	def generateDeck(self):
		suits = ['Clubs', 'Hearts', 'Diamonds', 'Spades']
		symbols = ['9', '10', 'J', 'Q', 'K', 'A']
		deck = []

		for suit in suits:
			for symbol in symbols:
				deck.append(card.Card(suit, symbol))

		return deck

	# method to start a round of Euchre
	def startRound(self):
		self.deal()
		self.faceup = self.deck[20]

	# method to evaluate who wins a hand
	# expects arguments as tuples in form ('Player Instance', 'Card Instance')
	def evaluteHand(card1, card2, card3, card4):
		winning = card1

	# method to evaluate which card beats the other
	# method returns True if card1 wins, False if card2 wins
	# expects arguments in the following form,
	#    card1, card2 as an instance of Card
	#    suitLed as one of ['Clubs', 'Hearts', 'Diamonds', 'Spades']
	def evaluateCards(card1, card2, suitLed):
		pass



	# method to deal a hand for a round	
	def deal(self):
		shuffle(self.deck)
		self.team1.player1.hand = self.deck[0:5]
		self.team1.player2.hand = self.deck[5:10]
		self.team2.player1.hand = self.deck[10:15]
		self.team2.player2.hand = self.deck[15:20]


	# method to display scores of teams
	def displayScores(self):
		print("Team 1: ", self.team1.gameScore, ", Team 2: ", self.team2.gameScore)
