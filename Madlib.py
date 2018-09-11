########################################################################
# Sarvath Sharma
# Computer Science 20
# March 20, 2017
# Credits: Oguzhan, Mr. Schellenberg, Alex
# Madlib
# Purpose: Take a familiar story and change the words to make it funny.
########################################################################
import random

userChoice = input("Type 1 for random or 2 for your own: ")

try:
    if userChoice == "2":
        adjective = input("Please Enter an adjective:")
        noun = input("Please enter a noun: ")
        animal = input("What is your favourite animal?")
        noise = input("Please enter any type of noise: ")
        vowel = input("Please enter a vowel: ")
        #This is where the user inputs will make a new story
        print(adjective + " Macdonald had a " + noun + ", " + vowel + " and on that " + noun + " he had an " + animal + " " + vowel +"  with a " + noise + noise + " here and a " + noise + noise + " there, here a " + noise + ", " + " there a " + noise + ", everywhere a " + noise  +  noise +  adjective + " Macdonald had a " + noun + ", " + vowel + ".")

    elif userChoice == "1":
        #You will have to change the area from where the code comes from (Poonam will be changed and so will the Documents
        randomAdjective = open("c:/Users/Poonam/Documents/Adjectives.txt", 'r')
        randomNoun = open("c:/Users/Poonam/Documents/Nouns.txt", 'r')
        randomAnimal = open("c:/Users/Poonam/Documents/Animlas.txt", 'r')
        randomNoise = open("c:/Users/Poonam/Documents/Noises.txt", 'r')
        randomVowvel = open("c:/Users/Poonam/Documents/Vowels.txt", 'r')
        #In this part, the list that was made will be used to pick random words for the Madlib
        chosenAdjective = random.choice(randomAdjective.readlines())
        chosenNoun = random.choice(randomNoun.readlines())
        chosenAnimal = random.choice(randomAnimal.readlines())
        chosenNoise = random.choice(randomNoise.readlines())
        chosenVowels = random.choice(randomVowvel.readlines())
        print(chosenAdjective + " Macdonald had a " + chosenNoun + ", " + chosenVowels + " and on that " + chosenNoun + " he had an " + chosenAnimal + " " + chosenVowels + " with a " + chosenNoise + " " + chosenNoise + " here and a " + chosenNoise + " " + chosenNoise + " there, here a " + chosenNoise + ", " + " and there a " + chosenNoise + ", everywhere a " + chosenNoise + " " + chosenNoise + " " + chosenAdjective + " Macdonald had a " + chosenNoun + ", " + chosenVowels + ".")

except ValueError:
    print("Enter something valid!")
