from dictionaries import europe
import random


class GameUser:
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.score = 0
        self.attempts = 3

    def level1(self, score, attempts):
        question_list = list(europe.items())
        options_list = list(europe.values())

        while True:
            if question_list != []:
                options = random.sample(options_list, 3)
                question_country, question_capital = random.choice(
                    question_list
                )

                for city in options:
                    if city == question_capital:
                        options.remove(city)
                        options.append(random.choice(options_list))

                options.append(question_capital)
                random.shuffle(options)
                options_letters = ["a", "b", "c", "d"]
                options_menu = dict(zip(options_letters, options))

                print(f"\nWhat is the capital of {question_country}?\n")

                for letter, option in options_menu.items():
                    print(f"{letter}) {option}")

                print(f"\n(End game at anytime by entering 0)")
                selection = input("Enter answer: ")

                if selection == "0":
                    return score
                elif selection == question_capital or (
                    selection in options_menu
                    and options_menu[selection] == question_capital
                ):
                    question_list.remove((question_country, question_capital))
                    score += 1
                    print(
                        f"You've answered correctly! Score: {score} -- Attempts left: {attempts}"
                    )
                    continue
                else:
                    attempts -= 1
                    if attempts <= 0:
                        try_again = input(
                            "Remaining attempts: 0. Game over. \nTry again? y/n "
                        )
                        if try_again == "n":
                            return score
                        else:
                            self.level1(0, 3)
                    else:
                        print(
                            f"Wrong answer. Remaining attempts: {attempts}. Score: {score}"
                        )
            else:
                print(
                    f"You've completed level 1 with a score of {score} points and {attempts} attempt(s) left"
                )
                return score
