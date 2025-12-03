# insert your comment header

# turtle boilerplate
import turtle

wn = turtle.Screen()
rory = turtle.Turtle()
# style/speed change on your own

def hollow_c(t):
    #draw a single block C shape
    t.fd(57.5)
    t.left(90)
    t.fd(100)
    t.left(90)
    t.fd(15)
    t.left(90)
    
    for i in range(3):
        t.fd(85)
        t.right(90)
    
    t.bk(15)
    t.right(90)
    
    t.fd(100)
    t.left(90)
    t.fd(57.5)
# main code
rory.right(90) #let's start facing south

turtle.tracer(False)
for i in range(0,360,25):
    hollow_c(rory)
    rory.left(25)
    turtle.update()

wn.exitonclick()



