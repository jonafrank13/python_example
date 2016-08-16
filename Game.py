from Players import Players
from Player  import Player

'''
@author::Jona
The Game class stores simulates the game based on details in Players class
'''

class Game:

	def __init__(self,players,target,max_balls):																											#constructor, target and balls can be specified
		self.players      = players
		self.target       = target
		self.max_balls    = max_balls

	def runGame(self,print_over = True):
		while (self.players.getNoOfPlayersInQueue() >= 2 and self.players.team_score <= self.target and self.players.team_balls_played <= self.max_balls):	#while 2 players left,target not achieved and balls available
			if(self.players.team_balls_played % 6 == 0 and print_over == True):																				#optional param check for problem 2, where target updates aren't required
				print (self.max_balls/6 - self.players.team_balls_played/6)," Overs remaining, ", self.target - self.players.team_score," Runs to win"		#print for over update
			self.players.getBallResult()
		print "Total Score = ",self.players.team_score,"/",self.players.getWickets()																		#print total
		self.players.printPlayers() 

	def printGameSummary(self):																																#print game result
		if(self.players.team_score > self.target):
			print self.players.team_name," won by ",self.players.getNoOfPlayersInQueue()," wickets !!!"
		elif(self.players.team_score == self.target):
			print "The match is drawn !!"
		else:
			print self.players.team_name," lost by ",self.target-self.players.team_score," runs !"

if __name__ == "__main__":																																	#test cases if run as standalone
	print('::::: Entering Game Class Test Mode :::::')
	player_1 = Player( 1 , "Kirat Boli"   , [5,30,25,10,15,1,9,5]  )
	player_2 = Player( 2 , "N.S Nodhi"    , [10,40,20,5,10,1,4,10] )
	player_3 = Player( 3 , "R Rumrah"     , [20,30,15,5,5,1,4,20]  )
	player_4 = Player( 4 , "Shashi Henra" , [30,25,5,0,5,1,4,30]   )
	test_players_list = [player_1,player_2,player_3,player_4]
	test_players      = Players(test_players_list,"Lengaburu")
	test_game  = Game(test_players,40,24)
	test_game.runGame()
	test_game.printGameSummary()