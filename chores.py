from random import randint
import player
class Chores:
    def __init__(self):
        self.num_chores_left = 5
        self.chores_and_numbers = {1:"Mopping", 2:"Scrubbing the toilet", 3:"Washing the windows"}
        self.chores_and_questions = {"Mopping":"When was the mop patented?", "Scrubbing the toilet":"Fill in the blank. _________ toilet.", "Washing the windows": "Which window needs to be cleaned? Please input 1, 2 or 3.\n [                   ]\n[................**]\n[                        ]"}
        self.chores_and_answers = {"Mopping": "1893", "Scrubbing the toilet":"skibidi", "Washing the windows":"2"}
        
    def doChore(self, player: player):
        if self.num_chores_left==0:
            print("The house is all clean. There are no chores to do.")
        else:
            print("\nAs you walk into the house, you spot the wet mop leaning near the door. \nA pile of newspapers and a bowl of fruit sit on top of the dining table, while a few flies roam above the rotting fruit inside the bowl.")
            print("Sighing, you decide to do a chore. Hard works pays off, right?")
            chore, question, answer = self.getChore()
            print("You decide to do " + chore + ".\n")
            self.num_chores_left-=1
            player_answer = input(question + "\n")
            if player_answer.lower()==answer:
                player.finishChore()
                print("Wow! That was a lot of hard work. Staring at the clean(er) house, you find a dollar bill in your hand.\n Stuffing it back into your pocket, you head back to town.")
            else:
                print("Well... I guess that wasn't too well of a job done. Maybe the house looks even worse than before. Awkwardly staring around, you quickly shuffle away towards town, hoping your mom doesn't get mad at you.\n\n Actually... where is she, anyways?")
    def getChore(self):
        chore_num = randint(1, 3)
        chore = self.chores_and_numbers[chore_num]
        question = self.chores_and_questions[chore]
        answer = self.chores_and_answers[chore]
        return chore, question, answer
        