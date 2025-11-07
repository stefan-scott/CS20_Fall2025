# Area of a Rectangle               TITLE
# November 4, 2025                  DATE
# Mr. Scott                         NAME
# A first look at python basics     1-line description

# Ask the user for w/h (store in vars)
# compute the area of that rectangle
# output the result to the screen

# Start by taking user input
# for the width and height
# *** input ALWAYS returns a string.
width = input("Enter a width:")
width = float(width)

height = input("Enter a height:")
height = float(height)

# before multiplying, we MUST ensure
# both width and height are NUMBERS.
area = width * height

# To practice user output, let's print
# the area in a nicely formatted
# sentence.
#
# STR + STR   is JOIN
# STR + Number   UNDEFINED

#            STR    + STR +  STR
# First way to print multiple strings (+)
message = "Area is " + str(area) + " units sq."
print(message)

# Second way to print multiple strings (,)
# - with this approach:
#       - don't need to convert types
#       - space seperates each item
print("Area is" , area , "units sq.")


