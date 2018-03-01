import os, sys
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from objects import game, team, player, card
import unittest

class CardEval(unittest.TestCase):
	player1 = player.Player('')
	player2 = player.Player('')
	player3 = player.Player('')
	player4 = player.Player('')
	team1 = team.Team(player1, player2)
	team2 = team.Team(player3, player4)
	current_game = game.Game(team1, team2)

	def test_is_left_bower(self):
		card1 = card.Card('Spades', 'J')
		self.current_game.trump =  'Clubs'
		result = self.current_game.isLeftBower(card1)
		self.assertEqual(result, True)

	def test_is_left_bower_2(self):
		card1 = card.Card('Clubs', 'J')
		self.current_game.trump =  'Spades'
		result = self.current_game.isLeftBower(card1)
		self.assertEqual(result, True)

	def test_is_left_bower_3(self):
		card1 = card.Card('Diamonds', 'J')
		self.current_game.trump =  'Hearts'
		result = self.current_game.isLeftBower(card1)
		self.assertEqual(result, True)

	def test_is_left_bower_4(self):
		card1 = card.Card('Hearts', 'J')
		self.current_game.trump =  'Diamonds'
		result = self.current_game.isLeftBower(card1)
		self.assertEqual(result, True)

	def test_is_left_bower_5(self):
		card1 = card.Card('Hearts', 'J')
		self.current_game.trump =  'Hearts'
		result = self.current_game.isLeftBower(card1)
		self.assertEqual(result, False)

	def test_is_left_bower_6(self):
		card1 = card.Card('Hearts', 'Q')
		self.current_game.trump =  'Hearts'
		result = self.current_game.isLeftBower(card1)
		self.assertEqual(result, False)

	def test_evaluate_cards(self):
		'''10 beats 9, same suit as led, neither trump'''

		card1 = card.Card('Spades', '9')
		card2 = card.Card('Spades', '10')
		self.current_game.trump = 'Hearts'
		result = self.current_game.evaluateCards(card1, card2, 'Spades')
		self.assertEqual(result, card2)
	
	def test_evaluate_cards_2(self):
		'''J beats 10, same suit as led, neither trump'''

		card1 = card.Card('Spades', '10')
		card2 = card.Card('Spades', 'J')
		self.current_game.trump = 'Hearts'
		result = self.current_game.evaluateCards(card1, card2, 'Spades')
		self.assertEqual(result, card2)

	def test_evaluate_cards_3(self):
		'''Should raise error when comparing two non-suit led, non-trump cards'''

		card1 = card.Card('Spades', '10')
		card2 = card.Card('Spades', 'J')
		self.current_game.trump = 'Hearts'
		with self.assertRaises(ValueError):
			self.current_game.evaluateCards(card1, card2, 'Diamonds')

	def test_evaluate_cards_4(self):
		'''9 beats 10, 9 follows suit & 10 doesn't, neither trump'''

		card1 = card.Card('Diamonds', '9')
		card2 = card.Card('Spades', '10')
		self.current_game.trump = 'Hearts'
		result = self.current_game.evaluateCards(card1, card2, 'Diamonds')
		self.assertEqual(result, card1)

	def test_evaluate_cards_5(self):
		'''9 beats 10, 10 follows suit & 9 doesn't, 9 trump'''

		card1 = card.Card('Hearts', '9')
		card2 = card.Card('Diamonds', '10')
		self.current_game.trump = 'Hearts'
		result = self.current_game.evaluateCards(card1, card2, 'Diamonds')
		self.assertEqual(result, card1)

	def test_evaluate_cards_6(self):
		'''J beats A, A follows suit & J does not, J right bower'''

		card1 = card.Card('Diamonds', 'A')
		card2 = card.Card('Hearts', 'J')
		self.current_game.trump = 'Hearts'
		result = self.current_game.evaluateCards(card1, card2, 'Diamonds')
		self.assertEqual(result, card2)

	def test_evaluate_cards_7(self):
		'''J beats A, A follows suit & J does not, J left bower'''

		card1 = card.Card('Diamonds', 'A')
		card2 = card.Card('Diamonds', 'J')
		self.current_game.trump = 'Hearts'
		result = self.current_game.evaluateCards(card1, card2, 'Diamonds')
		self.assertEqual(result, card2)

	def test_evaluate_cards_8(self):
		'''J beats A, both trump, J left bower'''

		card1 = card.Card('Hearts', 'A')
		card2 = card.Card('Diamonds', 'J')
		self.current_game.trump = 'Hearts'
		result = self.current_game.evaluateCards(card1, card2, 'Spades')
		self.assertEqual(result, card2)

	def test_evaluate_cards_9(self):
		'''J1 beats J2, both trump, J1 right bower and J2 left bower'''

		card1 = card.Card('Hearts', 'J')
		card2 = card.Card('Diamonds', 'J')
		self.current_game.trump = 'Hearts'
		result = self.current_game.evaluateCards(card1, card2, 'Spades')
		self.assertEqual(result, card1)

	def test_evaluate_cards_10(self):
		'''A beats Q, both trump'''

		card1 = card.Card('Clubs', 'A')
		card2 = card.Card('Clubs', 'Q')
		self.current_game.trump = 'Clubs'
		result = self.current_game.evaluateCards(card1, card2, 'Spades')
		self.assertEqual(result, card1)

	def test_evaluate_cards_11(self):
		'''Should raise error if comparing same cards, trump'''

		card1 = card.Card('Clubs', 'A')
		card2 = card.Card('Clubs', 'A')
		self.current_game.trump = 'Clubs'
		with self.assertRaises(ValueError):
			self.current_game.evaluateCards(card1, card2, 'Diamonds')

	def test_evaluate_cards_11(self):
		'''Should raise error if comparing same cards, not trump'''

		card1 = card.Card('Clubs', 'A')
		card2 = card.Card('Clubs', 'A')
		self.current_game.trump = 'Diamonds'
		with self.assertRaises(ValueError):
			self.current_game.evaluateCards(card1, card2, 'Diamonds')


if __name__ == '__main__':
	unittest.main()