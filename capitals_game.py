import random
from dictionaries import americas_caribbean

try_again = True
while try_again == True:
    attempts = 3
    score = 0

    question_list = list(americas_caribbean.items())
    options_list =  list(americas_caribbean.values())
    
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
                try_again = input("Game over. Try again? y/n ")
            else:
                print(f"Wrong answer. Remaining attempts: {attempts}")


        

        

        




