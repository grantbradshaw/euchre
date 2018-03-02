import os, sys
import unittest
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from objects import player
from environment import HEARTS, DIAMONDS, SPADES, CLUBS, A, K, Q, J, TEN, NINE, NOT_HELD

class PlayerInit(unittest.TestCase):
	
	def test_new_player_1(self):
		'''New player should have name they set'''
		player1 = player.Player('Jimothy')
		self.assertEqual(player1.name, 'Jimothy')

	def test_new_player_2(self):
		'''New player should be allowed blank names'''
		player1 = player.Player('')
		self.assertEqual(player1.name, '')

	def test_new_player_3(self):
		'''New player have error raised if they use reserved namespace'''
		with self.assertRaises(ValueError):
			player.Player(NOT_HELD)

if __name__ == '__main__':
	unittest.main()