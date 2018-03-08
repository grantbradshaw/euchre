import os, sys
import unittest
import copy
sys.path.append(os.path.abspath(os.path.dirname(__file__) + '/' + '..'))
from objects import player, card, team, game
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

class PlayCard(unittest.TestCase):
	player1 = player.Player('')
	player2 = player.Player('')
	player3 = player.Player('')
	player4 = player.Player('')
	team1 = team.Team(player1, player2)
	team2 = team.Team(player3, player4)
	current_game = game.Game(team1, team2)

	card1 = card.Card(CLUBS, NINE, player1)
	card2 = card.Card(CLUBS, A, player1)
	card3 = card.Card(SPADES, Q, player1)
	card4 = card.Card(DIAMONDS, TEN, player1)
	card5 = card.Card(HEARTS, K, player1)
	card6 = card.Card(DIAMONDS, J)
	card7 = card.Card(CLUBS, Q, player2)
	card8 = card.Card(HEARTS, NINE, player2)

	def test_play_card_1(self):
		'''Any card in hand should be valid if first to play, function should return any card from hand'''

		self.current_game.trump = SPADES
		# self.current_game.played = [] -> for reference, not required for function invocation
		available_cards = [self.card1, self.card2, self.card3, self.card4, self.card5]
		self.player1.hand = copy.copy(available_cards)
		result = self.player1.play(self.current_game.trump, None)
		self.assertIn(result, available_cards) # as card is removed from hand, need to use copy of hand

	def test_play_card_2(self):
		'''Card which is played should be appropriately removed from the hand'''

		self.current_game.trump = SPADES
		# self.current_game.played = [] -> for reference, not required for function invocation
		available_cards = [self.card1, self.card2, self.card3, self.card4, self.card5]
		self.player1.hand = copy.copy([self.card1, self.card2, self.card3, self.card4, self.card5])
		result = self.player1.play(self.current_game.trump, None)
		self.assertNotIn(result, self.player1.hand) # as card is removed from hand, test properly removed

	def test_play_card_3(self):
		'''Should only play one of the clubs cards when clubs are led'''

		self.current_game.trump = SPADES
		# self.current_game.played = [card7] -> for reference, not required for function invocation
		self.player1.hand = [self.card1, self.card2, self.card3, self.card4, self.card5]
		result = self.player1.play(self.current_game.trump, CLUBS)
		self.assertIn(result, [self.card1, self.card2])

	def test_play_card_4(self):
		'''Should only play a heart or the Jack of diamonds when hearts are led and trump'''

		self.current_game.trump = HEARTS
		# self.current_game.played = [card8] -> for reference, not required for function invocation
		self.player1.hand = [self.card2, self.card3, self.card4, self.card5, self.card6]
		result = self.player1.play(self.current_game.trump, HEARTS)
		self.assertIn(result, [self.card5, self.card6])

	def test_play_card_5(self):
		'''Should play any card when cannot follow suit'''

		self.current_game.trump = HEARTS
		# self.current_game.played = [card8] -> for reference, not required for function invocation
		available_cards = [self.card1, self.card2, self.card4, self.card5, self.card6]
		self.player1.hand = copy.copy(available_cards)
		result = self.player1.play(self.current_game.trump, SPADES)
		self.assertIn(result, available_cards)

	def test_select_card_1(self):
		'''selectCard method should raise exception if list of cards empty'''
		with self.assertRaises(ValueError):
			self.player1.selectCard([])

	def test_can_play_1(self):
		'''canPlay method should return True for J of Diamonds, trump clubs, suitLed Diamonds'''
		result = self.player1.canPlay(self.card6, CLUBS, DIAMONDS)
		self.assertEqual(result, True)

	def test_can_play_2(self):
		'''canPlay method should return False for J of Diamonds, trump clubs, suitLed Hearts'''
		result = self.player1.canPlay(self.card6, CLUBS, HEARTS)
		self.assertEqual(result, False)

	def test_can_play_3(self):
		'''canPlay method should return True for J of Diamonds, trump Hearts, suitLed Hearts'''
		result = self.player1.canPlay(self.card6, HEARTS, HEARTS)
		self.assertEqual(result, True)

	def test_can_play_4(self):
		'''canPlay method should return False for J of Diamonds, trump Hearts, suitLed Diamonds'''
		result = self.player1.canPlay(self.card6, HEARTS, DIAMONDS)
		self.assertEqual(result, False)

class DecideTrump(unittest.TestCase):
	player1 = player.Player('')
	player2 = player.Player('')
	player3 = player.Player('')
	player4 = player.Player('')
	team1 = team.Team(player1, player2)
	team2 = team.Team(player3, player4)
	current_game = game.Game(team1, team2)

	card1 = card.Card(CLUBS, NINE, player1)
	card2 = card.Card(CLUBS, A, player1)
	card3 = card.Card(SPADES, Q, player1)
	card4 = card.Card(DIAMONDS, TEN, player1)
	card5 = card.Card(HEARTS, K, player1)
	card6 = card.Card(DIAMONDS, J)
	card7 = card.Card(CLUBS, Q, player2)
	card8 = card.Card(HEARTS, NINE, player2)

	def test_decide_trump_face_up_1(self):
		'''Returns false if player does not have any of suit in hannd'''
		self.player1.hand = [self.card3, self.card4, self.card5, self.card6, self.card8]
		result = self.player1.decideTrumpFaceUp(self.card1, [self.player1, self.player2, self.player3, self.player4])
		self.assertEqual(result, False)

	def test_decide_trump_face_up_2(self):
		'''In current stubbbed implementation, should always return True if valid'''
		self.player1.hand = [self.card2, self.card4, self.card5, self.card6, self.card8]
		result = self.player1.decideTrumpFaceUp(self.card1, [self.player1, self.player2, self.player3, self.player4])
		self.assertEqual(result, True)

	def test_decide_trump_face_down_1(self):
		'''Returns any suit except the suit which was face up'''
		self.player1.hand = [self.card2, self.card4, self.card5, self.card6, self.card8]
		result = self.player1.decideTrumpFaceDown(self.card1, [self.player1, self.player2, self.player3, self.player4])
		self.assertIn(result, [SPADES, DIAMONDS, HEARTS])

	def add_card_to_hand(self):
		'''Player should have 5 cards in hand after being able to add card to hand'''
		self.player1.addCardToHand(card1, CLUBS, 0)
		selt.assertEqual(len(self.player1.hand), 5)


if __name__ == '__main__':
	unittest.main()