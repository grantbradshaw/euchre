class Team:
	'Base class for teams'

	def __init__(self, player1, player2):
		self.gameScore = 0
		self.tricks = 0
		self.calledTrump = False
		self.alone = False
		self.player1 = player1
		self.player2 = player2

	# method to determine how many points a team receives from a round and add it to the teams score
	# method returns nothing, has side effect of incrementing gameScore
	def scoreHand(self):
		if self.tricks < 3:
			pass
		elif self.tricks < 5:
			if self.calledTrump:
				self.gameScore += 1
			else:
				self.gameScore += 2
		elif self.tricks == 5:
			if self.alone == True:
				self.gameScore += 4
			else:
				self.gameScore += 2
		else:
			raise ValueError('Cannot have more than 5 tricks.')

	# method to determine if a player is on the team
	# method returns Boolean
	# expects arguments
	# 	player as an instance of Player
	def onTeam(self, player):
		return ((player == self.player1) or (player == self.player2))

	# method to determine if two players are on the same team, and not the same player
	# method retuns Boolean
	# expects arguments
	# 	player1, player2 as instances of Player
	def sameTeam(self, player1, player2):
		return self.onTeam(player1) and self.onTeam(player2) and player1 != player2






