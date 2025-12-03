# Multiple Turtles and For Loops
# Mr. Scott
# November 28, 2025

import turtle, random

# Create Screen
wn = turtle.Screen()
wn.bgcolor("black")
wn.setup(700, 700)

# Create some turtles
turtle_list = []
color_list = ["red", "green", "blue", "orange", "yellow", "grey", "white"]

NUM_TURTLES = 150 #ALL CAPS → constant 
angle = 360/NUM_TURTLES

turtle.tracer(False) #don't update screen
# Turtle Creation
for i in range(NUM_TURTLES):  #[0,1,2,3...]
    temp = turtle.Turtle()
    temp.color(random.choice(color_list))
    temp.left(i*angle)
    temp.up()
    temp.shape("turtle")
    turtle_list.append(temp)

# Loop through all turtles, give some instructions
for i in range(2000): #[0,1,2,3....,1998,1999]
    for t in turtle_list:
        t.fd(5)
        t.left(random.randrange(1,4)) #1-3
        if i % 10 == 0: #True once every 10 times
            t.stamp()
    turtle.update() #refresh the screen after each turtle moves

# At the very end...
wn.exitonclick()





