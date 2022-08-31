# import random
# from dictionaries import americas_caribbean, africa, europe, asia_middle_east, oceania_australia
# from classes import GameUser, Level


from curses.ascii import isdigit


print("୨⎯⎯‧̍̊˙˚˙ᵕ꒳ᵕ˙˚˙Welcome to the World Capitals Game!˙˚˙ᵕ꒳ᵕ˙˚˙‧̍̊⎯⎯୧")

while True:
    num_players = input("Number of players? ")
    if num_players.isdigit():
        if int(num_players) == 1:
            #Launch single mode player function
        elif int(num_players) > 1:
            #Launch multi player function
    else:
        print("Please enter a valid number of players.")
        continue

#while True:
    #Run high score function
    #Run leaderboard function
    #prompt user to exit or restart









    





        

        




