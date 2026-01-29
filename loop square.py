import turtle
from turtle import *
t = Turtle()

t.speed(0)

def square(x):
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)
    t.forward(x)
    t.left(90)


def doubleSquare(iRange):
    length=25
    for i in range(iRange):
        square(length,90)
        length=length*2
doubleSquare(5)




# for i in range(60):
#     square(50)
#     t.right(5)

# turtle.done()
# # //Refactor the previous loop to use a function called "Square"
# # Create a new function that uses a loop to create a triangle
# # Write a function that draws 60 squares, turning righjt 5 degrees after each square.
    
