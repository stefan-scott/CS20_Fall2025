# List Basics
# Nov 25, 2025
# Mr. Scott
# Creating, Accessing, Modifying Lists

fav_places = [] # empty list

# .append()  → adds a new item onto the end
fav_places.append("Saskatoon")  		#pos 0
fav_places.append("Iceland")    		#pos 1
fav_places.append("Volleyball Court")	#pos 2

# print(fav_places[1]) #[] indexing operator

# to delete, use .pop(index)
# fav_places.pop(0)
# print(fav_places[1])

# Exercise.  Ask the user for a number (0-2)
#            Remove that item from the list
#            Print out the list.    .pop(index)

# num = int(input("enter number 0-2: "))
# fav_places.pop(num)
# print(fav_places)

# Using the slicing operator, we can select
# a sub-list or sub-string   [start:end]
#                             inc : excl
print( "Centennial"[3:8] )
print( "Centennial"[:8] ) #from 0 to 7
print( "Centennial"[4:] ) #from 4 to end
#       0123456789




