import os, sys
import unittest
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from objects import game, team, player, card
from environment import HEARTS, DIAMONDS, SPADES, CLUBS, A, K, Q, J, TEN, NINE, SUITS, SYMBOLS


class CardEval(unittest.TestCase):
	player1 = player.Player('')
	player2 = player.Player('')
	player3 = player.Player('')
	player4 = player.Player('')
	team1 = team.Team(player1, player2)
	team2 = team.Team(player3, player4)
	current_game = game.Game(team1, team2)

	def test_evaluate_cards(self):
		'''10 beats 9, same suit as led, neither trump'''

		card1 = card.Card(SPADES, NINE)
		card2 = card.Card(SPADES, TEN)
		self.current_game.trump = HEARTS
		result = self.current_game.evaluateCards(card1, card2, SPADES)
		self.assertEqual(result, card2)

	def test_evaluate_cards_2(self):
		'''J beats 10, same suit as led, neither trump'''

		card1 = card.Card(SPADES, TEN)
		card2 = card.Card(SPADES, J)
		self.current_game.trump = HEARTS
		result = self.current_game.evaluateCards(card1, card2, SPADES)
		self.assertEqual(result, card2)

	def test_evaluate_cards_3(self):
		'''Should raise error when comparing two non-suit led, non-trump cards'''

		card1 = card.Card(SPADES, TEN)
		card2 = card.Card(SPADES, J)
		self.current_game.trump = HEARTS
		with self.assertRaises(ValueError):
			self.current_game.evaluateCards(card1, card2, DIAMONDS)

	def test_evaluate_cards_4(self):
		'''9 beats 10, 9 follows suit & 10 doesn't, neither trump'''

		card1 = card.Card(DIAMONDS, NINE)
		card2 = card.Card(SPADES, TEN)
		self.current_game.trump = HEARTS
		result = self.current_game.evaluateCards(card1, card2, DIAMONDS)
		self.assertEqual(result, card1)

	def test_evaluate_cards_5(self):
		'''9 beats 10, 10 follows suit & 9 doesn't, 9 trump'''

		card1 = card.Card(HEARTS, NINE)
		card2 = card.Card(DIAMONDS, TEN)
		self.current_game.trump = HEARTS
		result = self.current_game.evaluateCards(card1, card2, DIAMONDS)
		self.assertEqual(result, card1)

	def test_evaluate_cards_6(self):
		'''J beats A, A follows suit & J does not, J right bower'''

		card1 = card.Card(DIAMONDS, A)
		card2 = card.Card(HEARTS, J)
		self.current_game.trump = HEARTS
		result = self.current_game.evaluateCards(card1, card2, DIAMONDS)
		self.assertEqual(result, card2)

	def test_evaluate_cards_7(self):
		'''J beats A, A follows suit & J does not, J left bower'''

		card1 = card.Card(DIAMONDS, A)
		card2 = card.Card(DIAMONDS, J)
		self.current_game.trump = HEARTS
		result = self.current_game.evaluateCards(card1, card2, DIAMONDS)
		self.assertEqual(result, card2)

	def test_evaluate_cards_8(self):
		'''J beats A, both trump, J left bower'''

		card1 = card.Card(HEARTS, A)
		card2 = card.Card(DIAMONDS, J)
		self.current_game.trump = HEARTS
		result = self.current_game.evaluateCards(card1, card2, SPADES)
		self.assertEqual(result, card2)

	def test_evaluate_cards_9(self):
		'''J1 beats J2, both trump, J1 right bower and J2 left bower'''

		card1 = card.Card(HEARTS, J)
		card2 = card.Card(DIAMONDS, J)
		self.current_game.trump = HEARTS
		result = self.current_game.evaluateCards(card1, card2, SPADES)
		self.assertEqual(result, card1)

	def test_evaluate_cards_10(self):
		'''A beats Q, both trump'''

		card1 = card.Card(CLUBS, A)
		card2 = card.Card(CLUBS, Q)
		self.current_game.trump = CLUBS
		result = self.current_game.evaluateCards(card1, card2, SPADES)
		self.assertEqual(result, card1)

	def test_evaluate_cards_11(self):
		'''Should raise error if comparing same cards, trump'''

		card1 = card.Card(CLUBS, A)
		card2 = card.Card(CLUBS, A)
		self.current_game.trump = CLUBS
		with self.assertRaises(ValueError):
			self.current_game.evaluateCards(card1, card2, DIAMONDS)

	def test_evaluate_cards_12(self):
		'''Should raise error if comparing same cards, not trump'''

		card1 = card.Card(CLUBS, A)
		card2 = card.Card(CLUBS, A)
		self.current_game.trump = DIAMONDS
		with self.assertRaises(ValueError):
			self.current_game.evaluateCards(card1, card2, DIAMONDS)

	def test_evaluate_cards_13(self):
		'''Q beats J, same suit as led, neither trump'''

		card1 = card.Card(SPADES, J)
		card2 = card.Card(SPADES, Q)
		self.current_game.trump = HEARTS
		result = self.current_game.evaluateCards(card1, card2, SPADES)
		self.assertEqual(result, card2)

	def test_evaluate_cards_14(self):
		'''Q beats J, same suit as led, neither trump'''

		card1 = card.Card(SPADES, Q)
		card2 = card.Card(SPADES, K)
		self.current_game.trump = HEARTS
		result = self.current_game.evaluateCards(card1, card2, SPADES)
		self.assertEqual(result, card2)

	def test_evaluate_cards_15(self):
		'''Q beats J, same suit as led, neither trump'''

		card1 = card.Card(SPADES, K)
		card2 = card.Card(SPADES, A)
		self.current_game.trump = HEARTS
		result = self.current_game.evaluateCards(card1, card2, SPADES)
		self.assertEqual(result, card2)

class HandEval(unittest.TestCase):
	player1 = player.Player('')
	player2 = player.Player('')
	player3 = player.Player('')
	player4 = player.Player('')
	team1 = team.Team(player1, player2)
	team2 = team.Team(player3, player4)
	current_game = game.Game(team1, team2)

	def test_evaluate_hand(self):
		''' Trump Hearts, 9 of Hearts beats A of Spades, A of Clubs, A of Diamonds'''

		card1 = card.Card(HEARTS, NINE)
		card2 = card.Card(SPADES, A)
		card3 = card.Card(CLUBS, A)
		card4 = card.Card(DIAMONDS, A)
		self.current_game.trump = HEARTS
		self.current_game.played = [card1, card2, card3, card4]
		result = self.current_game.evaluateHand()
		self.assertEqual(result, card1)

	def test_evaluate_hand_2(self):
		''' Trump Hearts, 9 of Hearts beats A of Spades, A of Clubs, A of Diamonds'''

		card1 = card.Card(SPADES, A)
		card2 = card.Card(HEARTS, NINE)
		card3 = card.Card(CLUBS, A)
		card4 = card.Card(DIAMONDS, A)
		self.current_game.trump = HEARTS
		self.current_game.played = [card1, card2, card3, card4]
		result = self.current_game.evaluateHand()
		self.assertEqual(result, card2)

	def test_evaluate_hand_3(self):
		''' Trump Clubs, 9 of Hearts beats A of Spades, K of Spades, A of Diamonds, when 9 played first'''

		card1 = card.Card(HEARTS, NINE)
		card2 = card.Card(SPADES, A)
		card3 = card.Card(SPADES, K)
		card4 = card.Card(DIAMONDS, A)
		self.current_game.trump = CLUBS
		self.current_game.played = [card1, card2, card3, card4]
		result = self.current_game.evaluateHand()
		self.assertEqual(result, card1)

	def test_evaluate_hand_4(self):
		''' Trump Clubs, J of Spades beats A of Diamonds, K of Hearts, A of Clubs, when A of Diamonds played first'''

		card1 = card.Card(DIAMONDS, A)
		card2 = card.Card(CLUBS, A)
		card3 = card.Card(HEARTS, K)
		card4 = card.Card(SPADES, J)
		self.current_game.trump = CLUBS
		self.current_game.played = [card1, card2, card3, card4]
		result = self.current_game.evaluateHand()
		self.assertEqual(result, card4)

class RuleEval(unittest.TestCase):
	player1 = player.Player('')
	player2 = player.Player('')
	player3 = player.Player('')
	player4 = player.Player('')
	team1 = team.Team(player1, player2)
	team2 = team.Team(player3, player4)
	current_game = game.Game(team1, team2)

	# method to compare if two instances of cards have same suit and symbol
	# returns a Boolean
	# expects arguments
	# 	card1, card2 as instances of card
	def cardsEqual(self, card1, card2):
		return ((card1.suit == card2.suit) and (card1.symbol == card2.symbol))

	# method should return if a card is valid
	# returns a Boolean
	# expects arguments
	# 	card as instance of card
	def cardValid(self, card):
		return ((card.suit in SUITS) and (card.symbol in SYMBOLS))

	def test_generate_deck(self):
		'''Deck should contain 24 unique, valid cards'''
		self.current_game.generateDeck()
		result = []
		for card in self.current_game.deck:
			if self.cardValid(card) and (len(list(filter(lambda x: self.cardsEqual(x, card), result)))) == 0:
				result.append(card)

		self.assertEqual(24, len(result))

	def test_start_round_1(self):
		'''Each player should have 5 cards in hand'''
		self.current_game.startRound()
		for player in [self.player1, self.player2, self.player3, self.player4]:
			with self.subTest(player=player):
				self.assertEqual(len(player.hand), 5)

	def test_start_round_2(self):
		'''Faceup card should be different from any card in players hands'''
		self.current_game.startRound()
		result = False # result indicates whether card has appeared in a hand
		for player in [self.player1, self.player2, self.player3, self.player4]:
			for card in player.hand:
				if self.cardsEqual(card, self.current_game.faceup):
					result = True
		self.assertEqual(result, False)

	def test_start_round_3(self):
		'''There should be 4 players at the table'''
		self.current_game.startRound()
		self.assertEqual(4, len(self.current_game.table))

	def test_start_round_4(self):
		'''The last player at the table should be the dealer'''
		self.current_game.startRound()
		self.assertEqual(self.current_game.table[-1], self.current_game.dealer)

	def test_start_round_5(self):
		'''Players following each other in the table should not be on the same team'''
		self.current_game.startRound()
		lastPlayer = self.current_game.table[-1] # should test dealer
		for player in self.current_game.table:
			with self.subTest(player=player):
				self.assertNotEqual(self.team1.onTeam(player), self.team1.onTeam(lastPlayer))
				lastPlayer = player

	def test_start_round_6(self):
		'''A second round should have a different dealer'''
		self.current_game.startRound()
		dealer1 = self.current_game.dealer
		self.current_game.startRound()
		self.assertNotEqual(dealer1, self.current_game.dealer)

if __name__ == '__main__':
	unittest.main()