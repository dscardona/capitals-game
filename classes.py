import random
class GameUser: 
    def __init__(self, name, level):
        self.name = name
        self.level = level
        self.score = 0
        self.attempts = 3

class Level:
    def __init__(self, username, region, answer_mode, question_mode):
        self.username = username
        self.region = region
        self.answer_mode = answer_mode
        self.question_mode = question_mode

    def generate_question(self):
        question_list = list(self.region.items())
        options_list =  list(self.region.values())

        while len(question_list) != 0:
            question_country, question_capital = random.choice(question_list)
            options = random.sample(options_list, 3)
            options.append(question_capital)
            random.shuffle(options)
            option_letters = ["d", "c", "b", "a"]

                
        print(f'\nWhat is the capital of {question_country}?\n')
        
        for option in options:
            option_number = option_letters.pop()
            print(f'{option_number}) {option}')
                     
        selection = input("Enter answer: ")

        if selection == question_capital:
            print("You've answered correctly!")
            question_list.remove((question_country, question_capital))
            score += 1
        else:
            attempts -= 1
            if attempts <= 0:
                try_again = input("Remaining attempts: 0. Game over. \nTry again? y/n ")
            else:
                print(f"Wrong answer. Remaining attempts: {attempts}")


class Level1(Level):
    def __init__(self, username, region, answer_mode, question_mode):
        super().__init__(username, region, answer_mode, question_mode)

#Level1 Class
    #attributes below defined in user class
    #Name displayed
    #Score displayed
    #Attempts displayed
    
    #Multiple choice question generated - function
        #considers level: multiple choice, only Europe, pick from capitals
        #updates counters
        #updates leaderboard (current game/and global)
        #updates high score (personal, historic)

        #End of game
            #manually
            # out of attempts 


#Level2 Class
    #attributes below defined in user class
    #Name displayed
    #Score displayed
    #Attempts displayed
    
    #Multiple choice question generated - function
        ##considers level: multiple choice, world, pick from capitals
        #updates counters
        #updates leaderboard (current game/and global)
        #updates high score (personal, historic)

        #End of game
            #manually
            # out of attempts

#level3 Class
    #attributes below defined in user class
    #Name displayed
    #Score displayed
    #Attempts displayed
    
    #Multiple choice question generated - function
        #considers level: multiple choice, world, pick from countries and capitals
        #updates counters
        #updates leaderboard (current game/and global)
        #updates high score (personal, historic)

        #End of game
            #manually
            # out of attempts

#level4 Class
    #attributes below defined in user class
    #Name displayed
    #Score displayed
    #Attempts displayed
    
    #Multiple choice question generated - function
        #considers level: prompts user to type answer
        #updates counters
        #updates leaderboard (current game/and global)
        #updates high score (personal, historic)

        #End of game
            #manually
            # out of attempts
    

