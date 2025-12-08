# Lists and Slicing Practice
# Mr. Scott
# Dec 8, 2025

# 2 Types of Collections
# lists     strings
foods = ["apple", "banana", "cantaloupe", "dragonfruit"]
#           0         1          2             3
#          -4         -3         -2           -1

city = "Saskatoon"
#       012345678
# Recap Looping through Collection
# Loop by item
for item in foods:  #[0,1,2,3]
    print(item)

for letter in city: 
    if(letter == "o" or letter == "a"):
        print(letter)

# Loop by index    4
for i in range(len(foods)):  #[0,1,2,3]
    fruit = foods[i]
    if i == len(foods)-1:
        print(fruit.upper())
    else:
        print(fruit)
        

# Slicing:  get sub-list or sub-string
# name_of_collection[start:end]
#                   [inc : excl]


# 5 MINUTE CHALLENGE
new_list = [11,33,55,77,99,121,143]#X
#            0  1  2  3  4  5   6   7

new_word = "Centennial Collegiate"
#           0123456789
# print out the follow via slicing:
#
print(new_list[3:])
# 1.  [77,99,121,143]
print(new_word[9:12])
# 2.  "l C"
print(new_word[11:])
# 3.  "Collegiate"




