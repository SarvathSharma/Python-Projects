import turtle, random
FINISHLINE = 300
wn = turtle.Screen()
wn.bgcolor("lightgreen")

#One of the contestants
sarvath = turtle.Turtle()
sarvath.penup()
sarvath.color("blue")
sarvath.shape("turtle")
sarvath.goto(-300, -10)

#One of the contestants
noah = turtle.Turtle()
noah.penup()
noah.color("green")
noah.shape("turtle")
noah.goto(-300, 10)

#The ref will make a line
ally = turtle.Turtle()
ally.shape("turtle")
ally.hideturtle()
ally.penup()
ally.color("red")
ally.goto(FINISHLINE, 40)
ally.pendown()
ally.goto(FINISHLINE, -40)

#This is where the race begins and ends
theWinner = False
while theWinner == False:
    noahstep = random.randint(1, 7)
    sarvathstep = random.randint(1, 7)

    noah.forward(noahstep)
    sarvath.forward(sarvathstep)

    if noah.xcor() >= FINISHLINE:
        print("Noah wins!")
        theWinner = True
    if sarvath.xcor() >= FINISHLINE:
        print("Sarvath wins!")
        theWinner = True

theWindow.mainloop()