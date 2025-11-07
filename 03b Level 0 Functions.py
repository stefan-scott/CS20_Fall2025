# Fortune Teller Machine
# Mr. Scott
# Nov 6, 2025

# Revisit "level 0" function
#     - function with no inputs, no outputs
#     - useful for reuse of code, organization

def fortune_one():
    #print out a fortune for the user
    print("today will be lucky!")

def fortune_two():
    #print another one
    print("don't step on the cracks...")

# ---- MAIN CODE STARTS HERE ----

# use random numbers to select a fortune
import random as r
flip = r.randrange(0,2) # 0, 1

if flip == 0:
    fortune_one()
elif flip == 1:
    fortune_two()
    
# another comment to describe next section
# if there is one...