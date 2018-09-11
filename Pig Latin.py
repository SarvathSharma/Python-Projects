#######################################################
# Sarvath Sharma
# Computer Science 20
# May 5, 2017
# Credits: Alex and Golden
# Pig Latin Translator
# Purpose: Translate any given phrase into pig latin.
#######################################################

def getPrefix(aWord):
    '''Return the prefix of a word as a string. The prefix is defined as the letters in the word up to, but not including, the first vowel.
    >>> getPrefix("tree")
    'tr'
    >>> getPrefix("string")
    'str'
    >>> getPrefix("happy")
    'h'
    >>> getPrefix("I")
    ''
    '''
    punctuations = ',.?!'
    vowels = 'aeiouyAEIOUY'
    newWord = ""
    prefix = ""
    aWord = aWord.rstrip(punctuations)
    firstLetter = aWord[0]
    for letters in aWord:
        if firstLetter in vowels:
            prefix = ""
        elif letters not in vowels:
            newWord += letters
        elif letters in vowels:
            # Once all the letters up till, but not including the vowel are collected it will be returned
            prefix += newWord
            return prefix

def getStem(aWord):
    '''Return the stem of a word as a string. The stem is defined as the letters in the word after, and including, the first vowel.
    >>> getStem("tree")
    'ee'
    >>> getStem("string")
    'ing'
    >>> getStem("happy")
    'appy'
    >>> getStem("I")
    'I'
    '''
    punctuations = ',.?!'
    vowels = 'aeiouyAEIOUY'
    stem = ""
    aWord = aWord.rstrip(punctuations)
    vowelLocation = 0
    for letter in aWord:
        if letter in vowels:
            vowelLocation = vowelLocation
            # Once the location of the first letter is found every other letter (including the vowel) is returned
            stem += aWord[vowelLocation:]
            return stem
        else:
            # If the certain letter is not a vowel 1 will be added to find the location of the first vowel
            vowelLocation += 1

def translateWord(aWord):
    '''Return the word with the prefix and stem reversed, and with the appropriate word ending (either 'ay' or 'yay').
    >>> translateWord("tree")
    'eetray'
    >>> translateWord("string")
    'ingstray'
    >>> translateWord("happy")
    'appyhay'
    >>> translateWord("ultimate")
    'ultimateyay'
    >>> translateWord("I")
    'Iyay'
    '''
    vowels = 'aeiouyAEIOUY'
    punctuations = ',.?!'
    prefix = getPrefix(aWord)
    stem = getStem(aWord)
    punctuationTranslate = ""
    capitalWord = ""
    firstLetter = aWord[0]
    # Checkes if any character is not in the alphabet
    if aWord.isalpha() != True:
            # If the certain character is not in the alphabet it will be returned the way it came
            return aWord
    if aWord.isalpha() != True and aWord in punctuations:
            aWord = aWord.rstrip(punctuations)
            punctuationTranslate += punctuationPlacer(aWord)
            return punctuationPlacer
    for characters in aWord:
        if firstLetter.isupper() == True:
            # If the first letter is capitalized, then all letters will be lowercaed, translated and returned with the beginning capital letter
            aWord.lower()
            capitalWord += capitalizeWord(aWord)
            return capitalWord.capitalize()
        elif firstLetter in vowels:
            # If the first letter of the word is a vowel 'yay' will be added at the end
            return aWord + 'yay'
        elif firstLetter not in vowels:
            # If the first letter is not a vowel, the pig latin version of the word will be returned
            return stem + prefix + 'ay'

def capitalizeWord(aWord):
    '''If the first letter of the word is capital this code gets the code lowercased word, translates it and returns it so the other function
    can capitalize the word.
    >>> capitlalizeWord("Sarvath")
    'Arvathsay'
    >>> capitalizeWord("You")
    'Youyay'
    >>> capitalizeWord("No Littering")
    'Onay Itteringlay'
    '''
    vowels = 'aeiouyAEIOUY'
    prefix = getPrefix(aWord)
    stem = getStem(aWord)
    firstLetter = aWord[0]
    if firstLetter in vowels:
        return aWord + 'yay'
    elif firstLetter not in vowels:
        return stem + prefix + 'ay'

def punctuationPlacer(aWord): # Will only return the word with the punctuation untraslated
    ''' Places the punctuation at the right space and has a tranlated word.
    --> punctuationPlacer("No shirts, no shoes, no service")
    'Onay irtsshay, onay oesshay, onay ervicesay'
    '''
    punctuations = ',.?!'
    vowels = 'aeiouyAEIOUY'
    aWord = aWord.rstrip(punctuations)
    prefix = getPrefix(aWord)
    stem = getStem(aWord)
    firstLetter = aWord[0]
    if firstLetter in vowels:
        return aWord + 'yay' + punctuations
    elif firstLetter not in vowels:
        return stem + prefix + 'ay' + punctuations

def translateSentence(aSentence):
    '''Return the word with the prefix and stem reversed, and with the appropriate word ending (either 'ay' or 'yay').
    >>> translateSentence("no littering")
    'onay itteringlay'
    >>> translateSentence("stop")
    'opstay'
    >>> translateSentence("computer science is fun")
    'omputercay iencescay isyay unfay'
    >>> translateSentence("you can do this")
    'youyay ancay oday isthay'
    '''
    vowels = 'aeiouyAEIOUY'
    pigLatinSentence = ""
    wordByWord = aSentence.split()
    for words in wordByWord:
        # Each word in the sentence is split up and sent to the translateWord(aWord) to be translated properly
        pigLatinSentence += translateWord(words) + " "
    return pigLatinSentence

aSentence = input("Enter a sentence/word: ")
print( translateSentence(aSentence) )
#I attempted the punctuation part, but had to help my family and did not have time. Sorry I will try to do it this weekend.