import turtle

#Game is not done this is hopfulley going to be done in time for the major project assiment#
#NOT FINAL PRODUCT#

canvas = turtle.Screen()
canvas.bgcolor("black")
'''Set up screen'''
playerOne=turtle.Turtle()
playerTwo=turtle.Turtle()
wall=turtle.Turtle()
playerOne.turtlesize(.5)
playerTwo.turtlesize(.5)
playerOne.color("red")
playerTwo.color("blue")
wall.color("white")
playerOne.penup()
playerTwo.penup()
playerTwo.setheading(180)
playerOne.goto(-100,0)
playerTwo.goto(100,0)
playerOne.pendown()
playerTwo.pendown()
playerOne.pensize(5)
playerTwo.pensize(5)
''' set up the turtle in correct spot and correct input to allow game to start propley'''

def playerTwoLeft():
    playerTwo
    playerTwo.setheading(180)
    ''' Set the Tron facing left'''

def playerTwoRight():
    playerTwo
    playerTwo.right(90)
    ''' Set the Tron facing right'''

def playerTwoUp():
    playerTwo
    playerTwo.setheading(90)
    ''' Set the Tron facing up'''

def playerTwoDown():
    playerTwo
    playerTwo.setheading(270)
    ''' Set the Tron facing down'''

def playerOneLeft():
    playerOne
    playerOne.setheading(180)
    ''' Set the Tron facing left'''

def playerOneRight():
    playerOne
    playerOne.setheading(0)
    ''' Set the Tron facing right'''

def playerOneUp():
    playerOne
    playerOne.setheading(90)
    ''' Set the Tron facing up'''

def playerOneDown():
    playerOne
    playerOne.setheading(270)
    ''' Set the Tron facing down'''

playerOne.speed(0)
playerTwo.speed(0)
wall.speed(0)
wall.penup()
wall.goto(300,300)
wall.setheading(180)
wall.pendown()
wall.pensize(5)
for x in range(4):
    wall.forward(600)
    wall.left(90)
wall.hideturtle()
screen=playerTwo.getscreen()
screen.onkey(playerTwoLeft,"Left")
screen.onkey(playerTwoRight,"Right")
screen.onkey(playerOneLeft,"a")
screen.onkey(playerOneRight,"d")
screen.onkey(playerOneUp,"w")
screen.onkey(playerOneDown,"s")
screen.onkey(playerTwoUp,"Up")
screen.onkey(playerTwoDown,"Down")
screen.listen()
playerLine=[]
global playerLine
playerLineTwo=[]
global playerLineTwo

while True:
    playerTwo.forward(3)
    playerOne.forward(3)
    x,y=playerTwo.pos()
    q,w=playerOne.pos()
    x=int(x)
    y=int(y)
    l=(x,y)
    q=int(q)
    w=int(w)
    k=(q,w)
    if k in playerLine:
        print ("Game over")
        break
    elif l in playerLine:
        print("game over")
        break
    elif l in playerLineTwo:
        print("game over")
        break
    elif k in playerLineTwo:
        print("game over")
        break
    elif playerLineTwo == playerOne.pos():
        print("ewfw")
        break
    else:
        pass




    playerLine.append(l)
    playerLineTwo.append(k)

#player one is red#

turtle.mainloop()



