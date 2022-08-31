from curses.ascii import isdigit
from functions import high_score, leaderboard, single_player, multi_player


print("୨⎯⎯‧̍̊˙˚˙ᵕ꒳ᵕ˙˚˙Welcome to the World Capitals Game!˙˚˙ᵕ꒳ᵕ˙˚˙‧̍̊⎯⎯୧")
while True:
    while True:
        name = []
        score = []
        num_players = input("Number of players? 1 - 4 ")
        if num_players.isdigit() and int(num_players) != 0:
            if int(num_players) == 1:
                single_player()
            elif int(num_players) > 1:
                multi_player()
        else:
            print("Please enter a valid number of players.")
            continue

        high_score(name, score)
        leaderboard(name, score)
        
        play_again = input("Play again? y/n ")
        if play_again == "n":
            exit()
        elif play_again== "y":
            continue










    





        

        




