def get_num_players():
    #tried to call funcion recursively when the number of players is invalid. This was causing a type error (function returned None). This is why I opted for an infinite loop instead.
    while True:
        num_players = input("Number of players (4 max)? ")
        if num_players.isdigit():
            num_players = int(num_players)
            if num_players <= 4 and num_players > 0:
                print(f'Configuring game for {num_players} player(s)')
                return num_players
            print(f'Game can\'t support {num_players} players')
        else:
            print("Please enter a valid number of players.")

def get_name():
    while True:
        name = input("Enter name: ")
        if len(name) > 10:
            print("Names can't be over 10 characters")
        elif len(name) < 3:
            print("Names must have at least 3 characters")
        else:
            print(f"Hi, {name}. Welcome to the World Capitals Game!")
            return name

def get_level():
    while True:
        level = input("Enter level, 1 - 4: ")
        if level.isdigit():
            level = int(level)
            if level > 0 and level <= 4:
                return level
            else:
                print("Please enter a valid level number")
        else:
            print("Please enter a valid level number")

def multi_player():
    print("multi-player function pending")
    return

# def high_score(name, score):
    # print("high score function pending")
    # return

# def leaderboard(name, score):
    # print("leader board function pending")
    # return