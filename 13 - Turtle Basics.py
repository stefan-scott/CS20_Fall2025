# First Turtle
# Mr. Scott
# November 26, 2025
# A look at: window, turtle,  movement, color
#
# Reminder: NEVER save your file as turtle.py

import turtle #says: "load turtle.py"
import random

# Boilerplate Code → "Startup Code for using turtle"
window = turtle.Screen() #creates a screen object
window.bgcolor("cadetblue")
window.setup(600,400) #sets window dimensions

my_turtle = turtle.Turtle() #create a turtle object
my_turtle.color("yellow")
my_turtle.pensize(4) # thickness of the line
my_turtle.speed(0) # a bit like think() in Reeborg

turtle.tracer(False) #tracer is the thing that animates the turtle

# Main Program Starts...

# Program 01
colors = ["orchid", "palegoldenrod", "papayawhip", "gainsboro", "firebrick"]

num_moves = 40

for j in range(300):
    my_turtle.down() #pen onto the page
    
    for i in range(num_moves): #[0,1,2,3,...,num_moves-1]
        my_turtle.color(random.choice(colors))
        my_turtle.fd(5)
    my_turtle.up() #lifts the pen up
    my_turtle.goto(0,0)
    my_turtle.left(1)
    
    turtle.update() #when the tracer is OFF
                    #update() requests a manual screen refresh

    

# Program 02 - Few More Instructions
# my_turtle.bk(75)  #.backward()  .back()  .bk()
# my_turtle.rt(62)  #.rt()  .right()
# my_turtle.fd(110) #.fd()  .forward()
# my_turtle.goto(0,0) #absolute movement to (x,y)





# Program 01 - Basic Movement
# my_turtle.forward(100) #forward 100 pixels
# my_turtle.left(45)     #turn left 45 degrees
# my_turtle.backward(150)#backward 150 pixels





# At the VERY end of the program
window.exitonclick() #fixes the "hang" bug