class Team:
	'Base class for teams'

	def __init__(self, player1, player2):
		self.gameScore = 0
		self.tricks = 0
		self.calledTrump = False
		self.alone = False
		self.player1 = player1
		self.player2 = player2

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
		





	