import turtle

myCanvas = turtle.Screen()
larry = turtle.Turtle()
sidelength = 50
larry.speed(0)

def theCross():
    for counter in range(4):
        for angle in [90 , -90 , 90]:
            larry.forward(sidelength)
            larry.left(angle)

theCross()
larry.setheading(180)
theCross()
larry.setheading(270)
theCross()
larry.setheading(90)
theCross()

myCanvas.mainloop()