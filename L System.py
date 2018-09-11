def applyRules(letter):
    ''' Transforms a letter accordording to the rules of the systems.

    letter -> string'''
    if letter == "F":
        newLetter = "F-F++F-F"

    elif letter == "B":
        newLetter = "AB"

    else:
        newLetter = letter

    return newLetter

def processString(theString):
    ''' Applies ther rules to every character o astring.'''
    newString = ""
    for letter in theString:
        newString = newString + applyRules(letter)
    return newString

def createALSystem(axiom, numberOfIterations):
    ''' Process the L system by repeating a se6t of number of times.'''
    startingString = axiom
    for counter in range(numberOfIterations):
        newString = processString(startingString)
        startingString = newString
    return newString

def drawLSystem(someTurtle, theInstruction, angle, distance):
    ''' Interpret a string as turtle instructions'''
    for command in theInstruction:
        if command =="F":
            someTurtle.forward(distance)
        elif command == "B":
            someTurtle.backward(distance)
        elif command == "+":
            someTurtle.right(angle)
        elif command == "-":
            someTurtle.left(angle)

import turtle

theWindow = turtle.Screen()
sarvath = turtle.Turtle()
sarvath.speed(0)

sarvathsInstructions = createALSystem("F", 20)
drawLSystem(sarvath, sarvathsInstructions, 60, 5)


print( createALSystem("A", 15) )
