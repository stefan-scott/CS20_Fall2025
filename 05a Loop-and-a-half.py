# Loop and a Half
# Mr. Scott
# Nov 12, 2025
# "Forever" Loop, break, continue

# break → will exit the loop it is most immediately in
# continue → stops current iteration of the loop,
#            and begins the next one

while True:
    #"choice is set to the result of input" 
    choice = input("Stop the loop? [yes/no] ") #yes Yes YES yES 
    if choice.upper() == "YES":
        break
    elif choice.lower() == "maybe":
        continue
    print("Let's ask again...")
    