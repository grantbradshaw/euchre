import os, sys
import unittest
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from objects import card
from environment import HEARTS, DIAMONDS, SPADES, CLUBS, A, K, Q, J, TEN, NINE, NOT_HELD

class CardInit(unittest.TestCase):
	card1 = card.Card(SPADES, J, 'Jimothy')
	card2 = card.Card(SPADES, J, '')
	card3 = card.Card(SPADES, J)

	def test_new_card(self):
		'''Creating a card with holder "Not Held" raises an error'''
		with self.assertRaises(ValueError):
			card.Card(SPADES, J, NOT_HELD)

	def test_new_card_2(self):
		'''New card should have correct suit'''
		self.assertEqual(self.card1.suit, SPADES)

	def test_new_card_3(self):
		'''New card should have correct symbol'''
		self.assertEqual(self.card1.symbol, J)

	def test_new_card_4(self):
		'''New card should have correct holder'''
		self.assertEqual(self.card1.holder, 'Jimothy')

	def test_new_card_5(self):
		'''New card should set blank string holder to "Not Held"'''
		self.assertEqual(self.card2.holder, NOT_HELD)

	def test_new_card_6(self):
		'''New card without a holder should set holder to "Not Held"'''
		self.assertEqual(self.card3.holder, NOT_HELD)

class CardType(unittest.TestCase):

	def test_is_trump(self):
		'''K of Clubs is trump when trump is Clubs'''
		card1 = card.Card(CLUBS, K)
		result = card1.isTrump(CLUBS)
		self.assertEqual(result, True)

	def test_is_trump_2(self):
		'''K of Clubs is not trump when trump is Spades'''
		card1 = card.Card(CLUBS, K)
		result = card1.isTrump(SPADES)
		self.assertEqual(result, False)

	def test_is_trump_3(self):
		'''J of Clubs is trump when trump is Spades'''
		card1 = card.Card(CLUBS, J)
		result = card1.isTrump(SPADES)
		self.assertEqual(result, True)

	def test_is_trump_4(self):
		'''J of Clubs is trump when trump is Clubs'''
		card1 = card.Card(CLUBS, J)
		result = card1.isTrump(CLUBS)
		self.assertEqual(result, True)

	def test_is_trump_5(self):
		'''K of Clubs is not trump when trump is Hearts'''
		card1 = card.Card(CLUBS, J)
		result = card1.isTrump(HEARTS)
		self.assertEqual(result, False)

	def test_is_left_bower(self):
		'''J of Spades is a left bower when trump is Clubs'''
		result = card.Card(SPADES, J).isLeftBower(CLUBS)
		self.assertEqual(result, True)

	def test_is_left_bower_2(self):
		'''J of Clubs is a left bower when trump is Spades'''
		result = card.Card(CLUBS, J).isLeftBower(SPADES)
		self.assertEqual(result, True)

	def test_is_left_bower_3(self):
		'''J of Diamonds is a left bower when trump is Hearts'''
		result = card.Card(DIAMONDS, J).isLeftBower(HEARTS)
		self.assertEqual(result, True)

	def test_is_left_bower_4(self):
		'''J of Hearts is a left bower when trump is Diamonds'''
		result = card.Card(HEARTS, J).isLeftBower(DIAMONDS)
		self.assertEqual(result, True)

	def test_is_left_bower_5(self):
		'''J of Hearts is not a left bower when trump is Hearts'''
		result = card.Card(HEARTS, J).isLeftBower(HEARTS)
		self.assertEqual(result, False)

	def test_is_left_bower_6(self):
		'''Q cannot be a left bower'''
		result = card.Card(HEARTS, Q).isLeftBower(HEARTS)
		self.assertEqual(result, False)


if __name__ == '__main__':
	unittest.main()