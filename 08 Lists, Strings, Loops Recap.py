# Lists, Strings, Loops Recap
# Mr. Scott
# Nov 17, 2025
# Prep for our first Python Quiz

pet_names = ["Blizzard", "Scoops", "Logan", "Libby", "Archie"]
#                0           1        2        3         4
#                -5          -4       -3      -2        -1

# access list item:
# pet_names[3]  → accesses item at position 3
# pet_names[-1] → negative index counts positions from right to left
# len(pet_names) → returns # of items

# FOR LOOPS
# Repeat ONCE per item in a collection (list/string)
# current item is stored in the LOOP VARIABLE
# for current_pet in pet_names:
#     print(f"I love my pet {current_pet}")

# If you just want to repeat N times
# use range(n) → auto generates list w/ n things

# for i in range(15): #[0,1,2,3,4,5,...,14]
#     print(i)

# for i in range(5,10): #starts list at 5
#     print(i)        #up to (but not include) 10

for i in range(0, 100, 5): #start, end, step
    print(i)

