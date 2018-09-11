import turtle, random

wn = turtle.Screen()
wn.bgcolor = ("black")
sidelength = 150
sarvath = turtle.Turtle()
multipleColors = ["blue", "red", "black"]

for moving in range(5):
    sarvath.left(30)
    sarvath.forward(150/2)
    sarvath.left(90)
    sarvath.forward(sidelength)
    sarvath.color = random.choice(multipleColors)
    sarvath.right(90)
    sarvath.forward(sidelength)
    sarvath.color = random.choice(multipleColors)
    sarvath.left(90)

quit
