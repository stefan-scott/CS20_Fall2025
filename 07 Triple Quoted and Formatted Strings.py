# Triple Quoted and Formatted Strings
# Mr. SCott
# November 14, 2025
# More about text formatting + variables in text

# First, Triple Quoted
# There are 4 ways to enclose a string
# ""   ''   """ """   ''' '''
#         triple allow multi-line strings

my_str = '''He'd said my hair was "cool"
That was rather nice of him.
I had thought it looked a bit weird.'''
# print(my_str)


# -------- ESCAPE SEQUENCES --------
# using \ + another_char to insert something special
# \t → TAB  \n →NEWLINE  \" → "  \'→ '   \\→ \

my_str2 = "ab\tc\'\nd\"e\\fg"
# print(my_str2)


# Formatted Strings
# Joining text and variables nicely
food = "boba tea"
sport = "volleyball"
time_remaining = 6.7
import random

short_story = f"""My short story:
It's time for a {food} break.
The {sport} game is nearly done.
There are {time_remaining} minutes left.
We need {random.randrange(1,11)} more points.
"""


print(short_story)





