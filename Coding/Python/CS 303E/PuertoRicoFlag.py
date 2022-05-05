# File: PuertoRicoFlag.py
# Student: Cesar Gabriel Ayala-Mendoza
# UT EID: cga773
# Course Name: CS303E
#
# Date: 4/26/2022
# Description of Program: This program uses turtle graphics and its respective functions to draw the Puerto Rico Flag.

import turtle
import math

t = turtle.Turtle()

myBlue = '#00205B'      # sets the colors that were given to us
myRed = '#EF3340'
myWhite = '#FFFFFF'


def prepPos(x, y, colour):      # prepares the starting position of the turtle and color of pen and fill, takes the
    t.speed(50)                   # turtle up and then sets it down
    t.pensize(1)
    t.up()
    t.goto(x, y)
    t.down()
    t.pencolor(colour)
    t.fillcolor(colour)


def stripes(x, y, colour):
    prepPos(x, y, colour)   # turtle is prepared
    t.begin_fill()
    for i in range(2):  # this loop makes the shape of the rectangle by going forward and then turning 90 degrees
        t.forward(600)
        t.left(90)
        t.forward(80)
        t.left(90)
    t.end_fill()
    return


def triangle(x, y, colour):
    prepPos(x, y, colour)       # turtle is prepared
    t.begin_fill()
    t.left(30)
    for i in range(2):  # this loop makes the shape of the triangle by going forward in an angle, from the bottom
        t.forward(400)    # corner, and then turning and going to the top corner
        t.left(120)
    t.forward(400)
    t.end_fill()
    t.left(90)
    return


def star(x, y, colour):
    prepPos(x, y, colour)       # turtle is prepared
    t.left(180)
    t.begin_fill()
    t.forward(50)         # draws the 1st of 10 lines for the star
    for i in range(4):  # this loop does 8 of the 10 lines needed to draw the star by turning in different angles and
        t.left(144)       # then going forward
        t.forward(50)
        t.right(72)
        t.forward(50)
    t.left(144)
    t.forward(50)     # draws the last line of the star
    t.end_fill()
    return


stripes(0, 0, myRed)
stripes(0, 80, myWhite)     # calls the stripes functions to draw the 5 different stripes, color alternates and the
stripes(0, 160, myRed)      # starting position of the next stripe is where the last stripe ends
stripes(0, 240, myWhite)
stripes(0, 320, myRed)

triangle(0, 0, myBlue)      # draws the triangle with the respective color

X = (200 * math.sqrt(3)) / 2    # variable that helps calculate starting point of star
star(X - 60, 225, myWhite)      # draws star with respective color

t.hideturtle()

turtle.done()
