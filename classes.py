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

        


        