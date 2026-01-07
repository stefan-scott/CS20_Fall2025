# Accelerometer and Turtle Race
# Mr. Scott
# January 6, 2026
# Include a recap on FUNCTIONS

# accelerometers - measures orientation
# when flat:             reading ~ 0
# when 90 degrees left:  reading ~ -1048 
# when 90 degree right:  reading ~ +1048

# -1048     |       0      |       +1048
#         -300            300
#
#     LEFT        FLAT         RIGHT





import microbit, time, random, turtle

def x_tilt(dead_zone):
    # report the X-orientation of microbit
    # (left, flat, right)
    # dead_zone → positive number to determine
    #             how much tilt for non-flat reading
    x = microbit.accelerometer.get_x() #get_y() get_z()
    if x > dead_zone:
        return "right"
    elif x < dead_zone * -1:
        return "left"
    else:
        return "flat"
    
    
#Quick Turtle
t = turtle.Turtle()
s = turtle.Screen()
t.speed(0)
movement = 5

while True:
    current = x_tilt(300)
    print(current)
    #time.sleep(0.1)
    
    #turtle movement (accel)
    if current == "left":
        t.left(10)
    elif current == "right":
        t.right(10)
    t.fd(movement)
    
    #use y-tilt to change speed (movement var)
    
    #use buttons to change color / pen thickness
    
