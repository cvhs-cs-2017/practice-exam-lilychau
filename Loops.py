"""Use a loop to make a turtle draw a shape that is has at least 100 sides and
that shows symmetry.  The entire shape must fit inside the screen"""
import turtle
lily = turtle.Turtle()

for i in range(100):
    lily.forward(100)
    lily.right(60)
    lily.forward(60)
    lily.right(90)
    lily.forward(150)
    lily.right(100)
