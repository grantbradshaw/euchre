import os, sys
import unittest
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from objects import team, player
from environment import HEARTS, DIAMONDS, SPADES, CLUBS, A, K, Q, J, TEN, NINE, NOT_HELD

class ScoreTeam(unittest.TestCase):
	player1 = player.Player('')
	player2 = player.Player('')

	def test_team_score_1(self):
		'''Team which called trump and wins 3 tricks gets 1 point'''
		team1 = team.Team(self.player1, self.player2)
		team1.calledTrump = True
		team1.tricks = 3
		team1.scoreHand()
		self.assertEqual(team1.gameScore, 1)

	def test_team_score_2(self):
		'''Team which called trump and wins 4 tricks gets 1 point'''
		team1 = team.Team(self.player1, self.player2)
		team1.calledTrump = True
		team1.tricks = 4
		team1.scoreHand()
		self.assertEqual(team1.gameScore, 1)

	def test_team_score_3(self):
		'''Team which didn't call trump and wins 3 tricks gets 2 points'''
		team1 = team.Team(self.player1, self.player2)
		team1.calledTrump = False
		team1.tricks = 3
		team1.scoreHand()
		self.assertEqual(team1.gameScore, 2)

	def test_team_score_4(self):
		'''Team which calls trump and wins 5 tricks gets 2 points'''
		team1 = team.Team(self.player1, self.player2)
		team1.calledTrump = False
		team1.tricks = 5
		team1.scoreHand()
		self.assertEqual(team1.gameScore, 2)

	def test_team_score_5(self):
		'''Team which calls trump, goes alone, and wins 3 tricks gets 1 point'''
		team1 = team.Team(self.player1, self.player2)
		team1.calledTrump = True
		team1.tricks = 3
		team1.alone = True
		team1.scoreHand()
		self.assertEqual(team1.gameScore, 1)

	def test_team_score_6(self):
		'''Team which calls trump, goes alone, and wins 5 tricks gets 4 points'''
		team1 = team.Team(self.player1, self.player2)
		team1.calledTrump = True
		team1.tricks = 5
		team1.alone = True
		team1.scoreHand()
		self.assertEqual(team1.gameScore, 4)

	def test_team_score_7(self):
		'''Team which gets 2 tricks gets 0 points'''
		team1 = team.Team(self.player1, self.player2)
		team1.calledTrump = True
		team1.tricks = 2
		team1.scoreHand()
		self.assertEqual(team1.gameScore, 0)

	def test_team_score_8(self):
		'''Team with more than 5 tricks should raise an error'''
		team1 = team.Team(self.player1, self.player2)
		team1.tricks = 6
		with self.assertRaises(ValueError):
			team1.scoreHand()

if __name__ == '__main__':
	unittest.main()