import random

animals = ["dog", "cat", "rabbit"]

def guessAnimal():
    isGuess = True
    number = random.randint(0, 2)
    while (isGuess):
        answer = input("What is your answer? ")
        if (animals[number] == answer):
            print("Good Job, you guess it!")
            isGuess = False
        elif (animals[number] != answer):
            print('Bad guess')
    
guessAnimal()
