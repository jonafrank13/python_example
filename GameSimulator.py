from Game    import Game
from Player  import Player
from Players import Players

print('::::: PROBLEM 1 :::::')

player_1     = Player( 1 , "Kirat Boli"   , [5,30,25,10,15,1,9,5]  )
player_2     = Player( 2 , "N.S Nodhi"    , [10,40,20,5,10,1,4,10] )
player_3     = Player( 3 , "R Rumrah"     , [20,30,15,5,5,1,4,20]  )
player_4     = Player( 4 , "Shashi Henra" , [30,25,5,0,5,1,4,30]   )

players_list = [player_1,player_2,player_3,player_4]

players      = Players(players_list,"Lengaburu")

problem_1    = Game(players,40,24)

problem_1.runGame()
problem_1.printGameSummary()


print('::::: PROBLEM 2 :::::')

player_1_1     = Player( 1 , "Kirat Boli"   , [5,10,25,10,25,1,14,10]  )
player_2_1     = Player( 2 , "N.S Nodhi"    , [5,15,15,10,20,1,19,15]  )
player_1_2     = Player( 3 , "DB Vellyers"  , [5,10,25,10,25,1,14,10]  )
player_2_2     = Player( 4 , "H Mamla"      , [10,15,15,10,20,1,19,15] )

players_list_1 = [player_1_1,player_2_1]
players_list_2 = [player_1_2,player_2_2]

players_1 = Players(players_list_1,"Lengaburu")
players_2 = Players(players_list_2,"Enchai")

problem_2_1 = Game(players_1,999,12)
problem_2_1.runGame(False)

problem_2_2 = Game(players_2,problem_2_1.players.team_score,12)
problem_2_2.runGame()
problem_2_2.printGameSummary()