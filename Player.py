import random

'''
@author::Jona
This is the main player class
This has all the player data including the id,name,probability distribution,score etc of the player
The probability distribution variable has the player's probability for each score
Here the probability distribution variable has the structure
index 0 => O runs probability
index 1 => 1 run  probability
.
.
.
index 7 => Out probability
'''

class Player:

	def __init__(self, player_id , name , probability_distribution):																	#player constructor
		self.player_id                = player_id
		self.name                     = name
		self.probability_distribution = probability_distribution
		self.score                    = 0
		self.current_run              = 0
		self.balls_played             = 0
		self.is_out                   = False
		self.rotate_strike            = False

	def getResult(self):																												#main logic function for generating the random score
		sample_distribution = []																										#creating an sample list
		for index,probability in enumerate(self.probability_distribution):																
			sample               = [index]*probability 																					#populating list with the score(index)
			sample_distribution += sample 																								#appending to the sample distribution
		random.shuffle(sample_distribution) 																							#shuffling the sample, not required but still extra shuffle
		# print(sample_distribution)
		self.current_run   = random.sample(sample_distribution,1)[0] 																	#picking a random value from the distribution
		self.balls_played += 1 																											#incrementing the balls played
		return self.current_run

	def processResult(self):																											#processing the result
		if(self.current_run != 7):
			self.score += self.current_run																								#adding to the score
			if(self.current_run % 2 != 0):																								#rotating strike if required(for odd scores)
				self.rotate_strike = True
		else:
			self.is_out = True																											#setting the player as out
		self.printCommentary()

	def printCommentary(self):																											#commentary
		if(self.is_out == True):
			print self.name, " is OUT !!"
		else:
			print self.name, " scores ",self.current_run," run(s)"

	def printPlayerData(self):																											#print function
		print "player id                = " , self.player_id
		print "name                     = " , self.name
		print "probability distribution = " , self.probability_distribution
		print "score                    = " , self.score
		print "is out                   = " , self.is_out
		print "balls played             = " , self.balls_played
		print "strike rate              = " , 0 if self.balls_played == 0 else round((self.score/float(self.balls_played))*100,2) 		#calculating and printing the strike-rate of the player

if __name__ == "__main__":																												#test runner cases if run as stand alone file
	print('::::: Entering Player Class Test Mode :::::')																				#could have used unit test framework but avoided 3rd party imports
	testPlayer = Player(1, "JONA", [5,30,25,10,15,1,9,5])
	testPlayer.printPlayerData()
	print "Sample Ball Played :: "
	testPlayer.getResult()
	testPlayer.processResult()
	testPlayer.printPlayerData()