import os, sys
import unittest
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from objects import game, team, player, card
from environment import HEARTS, DIAMONDS, SPADES, CLUBS, A, K, Q, J, TEN, NINE


class CardEval(unittest.TestCase):
	player1 = player.Player('')
	player2 = player.Player('')
	player3 = player.Player('')
	player4 = player.Player('')
	team1 = team.Team(player1, player2)
	team2 = team.Team(player3, player4)
	current_game = game.Game(team1, team2)

	def test_is_left_bower(self):
		'''J of Spades is a left bower when trump is Clubs'''
		card1 = card.Card(SPADES, J)
		self.current_game.trump =  CLUBS
		result = self.current_game.isLeftBower(card1)
		self.assertEqual(result, True)

	def test_is_left_bower_2(self):
		'''J of Clubs is a left bower when trump is Spades'''
		card1 = card.Card(CLUBS, J)
		self.current_game.trump =  SPADES
		result = self.current_game.isLeftBower(card1)
		self.assertEqual(result, True)

	def test_is_left_bower_3(self):
		'''J of Diamonds is a left bower when trump is Hearts'''
		card1 = card.Card(DIAMONDS, J)
		self.current_game.trump =  HEARTS
		result = self.current_game.isLeftBower(card1)
		self.assertEqual(result, True)

	def test_is_left_bower_4(self):
		'''J of Hearts is a left bower when trump is Diamonds'''
		card1 = card.Card(HEARTS, J)
		self.current_game.trump =  DIAMONDS
		result = self.current_game.isLeftBower(card1)
		self.assertEqual(result, True)

	def test_is_left_bower_5(self):
		'''J of Hearts is not a left bower when trump is Hearts'''
		card1 = card.Card(HEARTS, J)
		self.current_game.trump =  HEARTS
		result = self.current_game.isLeftBower(card1)
		self.assertEqual(result, False)

	def test_is_left_bower_6(self):
		'''Q cannot be a left bower'''
		card1 = card.Card(HEARTS, Q)
		self.current_game.trump =  HEARTS
		result = self.current_game.isLeftBower(card1)
		self.assertEqual(result, False)

	def test_is_trump(self):
		'''K of Clubs is trump when trump is Clubs'''
		card1 = card.Card(CLUBS, K)
		self.current_game.trump = CLUBS
		result = self.current_game.isTrump(card1)
		self.assertEqual(result, True)

	def test_is_trump_2(self):
		'''K of Clubs is not trump when trump is Spades'''
		card1 = card.Card(CLUBS, K)
		self.current_game.trump = SPADES
		result = self.current_game.isTrump(card1)
		self.assertEqual(result, False)

	def test_is_trump_3(self):
		'''J of Clubs is trump when trump is Spades'''
		card1 = card.Card(CLUBS, J)
		self.current_game.trump = SPADES
		result = self.current_game.isTrump(card1)
		self.assertEqual(result, True)

	def test_is_trump_4(self):
		'''J of Clubs is trump when trump is Clubs'''
		card1 = card.Card(CLUBS, J)
		self.current_game.trump = CLUBS
		result = self.current_game.isTrump(card1)
		self.assertEqual(result, True)

	def test_is_trump_5(self):
		'''K of Clubs is not trump when trump is Hearts'''
		card1 = card.Card(CLUBS, J)
		self.current_game.trump = HEARTS
		result = self.current_game.isTrump(card1)
		self.assertEqual(result, False)


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


if __name__ == '__main__':
	unittest.main()