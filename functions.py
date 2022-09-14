def prompt_num_players():
    """Ask the user to enter the number of players.  Return the number if it is
    between 1 and 4 (inclusive), and None otherwise.
    """
    num_players = input("Number of players (4 max)? ")
    if not num_players.isdigit():
        print("Please enter a valid number of players.")
        return None

    num_players = int(num_players)
    if not 0 < num_players <= 4:
        print(f"Game can't support {num_players} players")
        return None

    print(f"Configuring game for {num_players} player(s)")
    return num_players


def get_num_players():
    num_players = prompt_num_players()
    while num_players is None:
        num_players = prompt_num_players()
    return num_players


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
