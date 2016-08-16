from Player import Player

'''
@author::Jona
The players class stores the team name,list of players playing, the team score and the balls faced
'''

class Players:

	def __init__(self,list_of_players,team_name):																			#constructor
		self.list_of_players   = list_of_players
		self.team_name         = team_name
		self.players_out       = []
		self.team_score        = 0
		self.team_balls_played = 0

	def printPlayers(self):																									#prints all the players in the team
		print "Players in ",self.team_name," : "
		for player in self.list_of_players:
			player.printPlayerData()
			print "*****************************************************************"
		for player in self.players_out:
			player.printPlayerData()
			print "*****************************************************************"

	def getPlayer(self,player_id):																							#gets player data given the id of the player
		for player in self.list_of_players:
			if(player.player_id == player_id):
				player.printPlayerData()
				return player
			else:
				print "Player player_id =",player_id," does not exist in the database"

	def removePlayer(self):																									#this is used to remove the player from the batting queue
		player = self.list_of_players[0]
		self.list_of_players.remove(player)
		self.players_out.append(player)

	def getNoOfPlayersInQueue(self):																						#returns number of players in batting queue
		return len(self.list_of_players)

	def getWickets(self):																									#self-explanatory
		return len(self.players_out)

	def getTotalPlayers(self):																								#gets total number of players in team
		return getNoOfPlayersInQueue()+getWickets()

	def getBallResult(self):																								#gets the current result of player and performs operations accordingly
		self.list_of_players[0].getResult()
		print "Over ",self.team_balls_played/6,".",(self.team_balls_played%6)+1," :: ",										
		self.list_of_players[0].processResult()
		self.team_balls_played += 1																							#incrementing the balls played by team
		if(self.list_of_players[0].is_out):																					#if player is out remove from batting queue and rotate strike in queue
			self.removePlayer()
			self.rotatePlayersInStrike()
		else:
			self.team_score += self.list_of_players[0].current_run															#update the team score
			if(self.list_of_players[0].rotate_strike):
				self.rotatePlayersInStrike()																				#if rotation required do so

	def rotatePlayersInStrike(self):																						#function rotates the 1st two players in queue
		if(len(self.list_of_players) >= 2):
			self.list_of_players[0] , self.list_of_players[1] = self.list_of_players[1] , self.list_of_players[0]

if __name__ == "__main__":																									#Test cases if run as a standalone file
	print('::::: Entering Players Class Test Mode :::::')
	player_1 = Player( 1, "JONA", [5,30,25,10,15,1,9,5] )
	list_of_players = [player_1]
	players = Players(list_of_players,"Chennai")
	print "List of players :: "
	players.printPlayers()
	print "Player 1 data :: "
	players.getPlayer(1)
	print "Players in queue :: ",players.getNoOfPlayersInQueue()
	players.removePlayer()
	print "Player 1 removed, remaining in queue :: ",players.getNoOfPlayersInQueue()
	print "Wickets :: ",players.getWickets()
	players_new = Players([Player( 2, "FRANK", [5,30,25,10,15,1,9,5] )],"Bangalore")
	players_new.printPlayers()
	players_new.getBallResult()
	players_new.printPlayers()