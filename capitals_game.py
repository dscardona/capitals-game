from classes import GameUser
from functions import get_level, get_num_players, multi_player, get_name

while True:
    # https://cutekaomoji.com/misc/sparkles/
    print(
        "୨⎯⎯‧̍̊˙˚˙ᵕ꒳ᵕ˙˚˙   Ⓦ ⓞ ⓡ ⓛ ⓓ  Ⓒ ⓐ ⓟ ⓘ ⓣ ⓐ ⓛ ⓢ  Ⓖ ⓐ ⓜ ⓔ   ˙˚˙ᵕ꒳ᵕ˙˚˙‧̍̊⎯⎯୧"
    )

    num_players = get_num_players()

    # Multiplayer Mode
    if num_players > 1:
        multi_player()

    # Single Player mode
    else:
        name = get_name()
        level = get_level()
        player = GameUser(name, level)
        print(f"Player {player.name} created. Selected level: {level}")
        if level == 1:
            score = player.level1(player.score, player.attempts)
        elif level == 2:
            print("level2 method pending")
        elif level == 3:
            print("level3 method pending")
        elif level == 4:
            print("level4 method pending")

    # high score/leaderboard function

    # option to restart or exit
    play_again = input("Press enter to play again, or 0 to exit ")
    if play_again == "0":
        break
