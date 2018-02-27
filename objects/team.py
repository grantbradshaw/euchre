class Team:
	'Base class for teams'

	def __init__(self, player1, player2):
		self.gameScore = 0
		self.handScore = 0
		self.player1 = player1
		self.player2 = player2

	