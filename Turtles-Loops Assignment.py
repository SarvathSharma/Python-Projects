########################################################################
# Sarvath Sharma
# Computer Science 20
# April 4, 2017
# Credits: www.stackoverflow.com and Alex
# Turtles/Loops Assignment
# Purpose: Making shapes with controls using the turtle program and loops
########################################################################

import turtle, random

#All the basic inputs for the program
myCanvas = turtle.Screen()
myCanvas.colormode(255)
sarvath = turtle.Turtle()
turtle = turtle.Turtle()
sarvath.shape("turtle")
myCanvas.bgcolor("black")
turtle.speed(0)
sarvath.speed(0)
randomShapesList = random.randint(1, 100)
colours = ["red", "blue", "gold", "pink", "green", "grey", "indianred", "lightgreen", "orange", "purple"]

#Random colours to choose from
r = random.randint(0, 255)
g = random.randint(0, 255)
b= random.randint(0, 255)
sarvath.color(r, g, b)

#This is the code for the code that makes one of the 2 shapes
def spiral():
    for shape in range(36):
        sarvath.pencolor(r, g, b)
        for square in range(4):
            sarvath.forward(200)
            sarvath.left(90)
        sarvath.right(10)

    size = 1

    for spin in range(300):
        turtle.pencolor(r, g, b)
        turtle.forward(size)
        turtle.right(91)
        size += 1

#This function runs by taking the User Input and make one of 2 shapes
def randomShapes():
    if randomShapesList >= 50:
        numberGiven = int(input("Please enter an angle for your shape (between 0 and 360): "))
        for forward in range(360):
            sarvath.pencolor(random.choice(colours))
            sarvath.width(2)
            sarvath.forward(forward)
            sarvath.left(numberGiven)

    elif randomShapesList <= 50:
        spiral()

    else:
        print("Program dead")

#This is the part where all the functions to use the keyborad comes in play
def moveUp():
    sarvath.forward(45)

def turnLeft():
    sarvath.left(45)

def turnRight():
    sarvath.right(45)

def moveBack():
    sarvath.back(45)


#Now to use the user input to make random shapes or use keys to do wacky stuff
userInput = input("Type 1 for random and 2 for keys control")

try:
    if userInput == "1":
        randomShapes()
        print("Here is your shape")

    elif userInput == "2":
        myCanvas.bgcolor("white")
        sarvath.pencolor(r, g, b)
        sarvath.speed(0)
        myCanvas.onkey(moveUp, "Up")
        myCanvas.onkey(turnLeft, "Left")
        myCanvas.onkey(turnRight, "Right")
        myCanvas.onkey(moveBack, "Down")
        myCanvas.listen()
        print("Up arrow is to move forward")
        print("Down arrow is to move backward")
        print("Left arrow is to roate left")
        print("Right arrrow is to rotate right")

    else:
        print("Something doesn't seem right.")

except ValueError:
        print("Number not valid")

myCanvas.mainloop()