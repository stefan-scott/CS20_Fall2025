# Regular Polygons
# Mr. Scott
# Dec 1, 2025

# Turtle Boilerplate
import turtle

wn = turtle.Screen()
wn.setup(700,700)

t = turtle.Turtle()

# On to the polygons
# FUNCTIONS
def triangle_simple():
    # using our turtle, draw a reg triangle
    # limitations:
    # - can control a specific global turtle
    # - size of the triangle is fixed (100)
    for i in range(3):
        t.fd(100)
        t.left(120)
    
def triangle_improved(active_turtle, length):
    # improved version of our function
    # any turtle can draw a reg triangle
    # side length can vary
    for i in range(3):
        active_turtle.fd(length)
        active_turtle.left(120)


def square(active_turtle, length):
    #use given turtle to draw square
    for i in range(4):
        active_turtle.fd(length)
        active_turtle.left(90)

def pentagon(active_turtle, length):
    #use given turtle to draw a pentagon
    for i in range(5):
        active_turtle.fd(length)
        active_turtle.left(72)

def regular_poly(active_turtle, n, length):
    # --- draw any regular polygon ---
    # active_turtle → (turtle) to do the drawing
    # n → (int), number of sides for polygon
    # length → (int) side length
    for i in range(n):
        active_turtle.fd(length)
        angle = 360/n
        active_turtle.lt(angle)

def cross(active_turtle, length):
    

# MAIN CODE
for i in range(3,30): 
    regular_poly(t, i, 50)
# triangle_improved(t, 150)
# square(t, 150)
# pentagon(t, 150)



# s = turtle.Turtle()
# s.color("orange")
# s.speed(0)
# t.speed(0)
#turtle.tracer(False)

# for side_length in range(5, 305, 5): #[5,10,15...295]
#     triangle_improved(t, side_length)
#     s.left(2)
#     triangle_improved(s, side_length)
    #turtle.update()

wn.exitonclick()
