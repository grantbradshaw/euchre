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


if __name__ == '__main__':
	unittest.main()