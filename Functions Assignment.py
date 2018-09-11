########################################################################
# Sarvath Sharma
# Computer Science 20
# April 13, 2017
# Credits: Alex, Python Docs
# Functions and Decisions/Selections Assignment
# Purpose: Using functions to make creatures with a certain amount of legs
########################################################################

import turtle, time

myCanvas = turtle.Screen()
sarvath = turtle.Turtle()
sarvath.speed(0)
myCanvas.bgcolor("white")
sarvath.shape("turtle")


def cleanUp(x, y):
    ''' This functions takes in the coordinates whenver it is called. It is used for the onclick function

    x -> X-Coordinate
    y -> Y-Coordinate
    '''
    while sarvath.undobufferentries() :
        sarvath.undo()


def drawLegs():
    ''' This funtion helps make the second function more effective by making the legs for the creature

    ex. drawLegs(numberOfLegsGiven) -> numberOfLegsGiven is where the user inputed number will help run the code to
    make the legs
    '''
    for legs in range(2):
        sarvath.color("black")
        sarvath.width(2)
        sarvath.right(60)
        sarvath.forward(50)
        sarvath.left(50)
        sarvath.forward(65)
        sarvath.back(65)
        sarvath.right(50)
        sarvath.back(50)
        sarvath.left(60)
        sarvath.left(90)
        sarvath.penup()
        sarvath.forward(180)
        sarvath.left(90)
        sarvath.pendown()


def drawCreature(aTurtle, numberOfLegs):
    ''' This function is where you enter a turtle name and a certain Number of Legs and it will make your creature

    ex. drawCreature(yourTurtleNameHere, 45)

    aTurtle -> turtle instance
    numberOfLegs -> int
    '''
    sarvath.color("black", "red")
    sarvath.begin_fill()
    sarvath.forward(180)
    sarvath.circle(90, 180)
    sarvath.forward(180)
    sarvath.circle(90,180)
    sarvath.fillcolor("red")
    sarvath.end_fill()
    sarvath.left(90)
    sarvath.color("blue")
    sarvath.begin_fill()
    sarvath.penup()
    sarvath.forward(45)
    sarvath.pendown()
    sarvath.circle(15)
    sarvath.penup()
    sarvath.forward(90)
    sarvath.pendown()
    sarvath.circle(15)
    sarvath.end_fill()
    sarvath.penup()
    sarvath.back(135)
    sarvath.pendown()
    sarvath.right(90)

    #In this area if the number inputed is odd, then you need to understand why creatures can't have odd number of legs (It's Science man)

    if numberOfLegs == 2:
        sarvath.forward(90)
        drawLegs()
        sarvath.penup()
        sarvath.forward(int(180/ (numberOfLegs/2)))
        sarvath.pendown()

    elif int(numberOfLegs % 2)  == False:
        for creature in range(int(numberOfLegs/2)):
            drawLegs()
            sarvath.penup()
            sarvath.forward(int(180/ (numberOfLegs/2)))
            sarvath.pendown()

    else:
        print("Even numbers only man")

numberOfLegs = int(turtle.numinput("Legs", "Please enter a number of legs"))
drawCreature(sarvath, numberOfLegs)
sarvath.write("Click me!!", True, align= "right", font="arial, 20")
time.sleep(1.5)
sarvath.onclick(cleanUp)

myCanvas.mainloop()