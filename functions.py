from curses.ascii import isdigit


def high_score(name, score):
    print("high score function pending")
    return

def leaderboard(name, score):
    print("leader board function pending")
    return

def single_player():
    while True:
        name = input("Enter name: ")
        if len(name) > 10:
            print("Names can't be over 10 characters")
        else:
            break

    while True:
        level = input("Enter level, 1 - 4: ")
        if level.isdigit() and int(level) > 0:
            if int(level) <= 1:
                print("Launch level 1, single player")
                break
            elif int(level) <= 2:
                print("Launch level 2, single player")
                break
            elif int(level) <= 3:
                print("Launch level 3, single player")
                break
            elif int(level) <= 4:
                print("Launch level 4, single player")
                break
            else:
                print("Level number can't be above 4.")
                continue
        else:
            print("Please enter a valid level number")
            continue

        #save in list, will be used in level class, high score variable, leaderboard function
    #Enter levels
        #used in the player mode function
    #Generate game corresponding to players and levels
    #Create user class, launch single level from inside user class
        #user class has score and attempts counters
        #Run level function inside user class
def multi_player():
    print("multi-player function pending")
    return
#Multiplayer
    #Enter name
        #save in list, will be used in level class, high score variable, leaderboard function
    #Enter levels
        #used in the player mode function
    #Generate game corresponding to players and levels
    #Create user classes, level stacking function
        #user class has score and attempts counters
        #Run level function inside user class