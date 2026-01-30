import turtle
from turtle import *
t = Turtle()

t.speed(0)

def star(x):
    t.forward(x)
    t.left(144)
    t.forward(x)
    t.left(144)
    t.forward(x)
    t.left(144)
    t.forward(x)
    t.left(144)
    t.forward(x)
    t.left(144)
star(25)

def doubleStar(iRange):
    length=(25)
    for i in range(iRange):
        star(length)
        t.right(3)
        length+=7
doubleStar(100)

turtle.done()


# for i in range(60):
#     square(50)
#     t.right(5)

# turtle.done()
# # //Refactor the previous loop to use a function called "Square"
# # Create a new function that uses a loop to create a triangle
# # Write a function that draws 60 squares, turning righjt 5 degrees after each square.
# Create a function that will draw a 5 pointed star using the angle 144. Then create a function that draw a spiral of stars that looks as follows