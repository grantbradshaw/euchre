# master filing for launching application

from objects import game, team, player, card


# master function to start a game of Euchre
def run():
	player1 = player.Player('')
	player2 = player.Player('')
	player3 = player.Player('')
	player4 = player.Player('')
	team1 = team.Team(player1, player2)
	team2 = team.Team(player3, player4)
	current_game = game.Game(team1, team2)

	
# execute program
run()