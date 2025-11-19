# Picking a name from a hat

import random

names = ["Stefan", "Aubree", "Megan", "Jeremiah"] #len == 4
#           0          1        2         3 (len-1)   X 4 X
#           0 ..... len-1
 
# Approach 1: random by index
index = random.randrange(0, len(names))
#print(names[index])

# Approach 2: random by choice
sibling = random.choice(names) #looks in a list, picks one
print(sibling)


