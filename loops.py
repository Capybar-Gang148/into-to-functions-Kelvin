import turtle
from turtle import *

t = Turtle()
t.shape("turtle")
t.speed (20)
# def square(x):
#     for i in range(1000):
#         t.forward(x)
#         t.left(90)
#         t.forward(x)
#         t.left(90)
#         t.forward(x)
#         t.left(90)
#         t.forward(x)
#         t.left(1)

# square(100)

# sidelength = 100
# rotate = 90
# def square(x,y):
#     for i in range(4):
#         t.forward(x)
#         t.left(y)
       
# square(100,90)

# def doubleSquares(iRange):
#     length = 5
#     for i in range(iRange):
#         square(length, 90)
#         length = length * 1.1
# doubleSquares(300)

# def addSquares(iRange):
#     length = 5
#     for i in range(iRange):
#         square(length, 90)
#         length += 5
#         t.right(5)
# addSquares(60)

def star(x,y):
    for i in range(5):
         t.forward(x)
         t.left(y)
    
def addStars (iRange):
    length = 5
    for i in range(iRange):
        star(length, 144)
        length += 5
        t.right(5)
addStars(1500)
turtle.done()