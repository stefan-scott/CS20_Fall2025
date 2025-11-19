# A2 Warmup
# Mr. Scott
# Nov 18, 2025

def create_story():
    # ask the user for 3 things
    # incorporate them into a story
    food = input("enter a food: ")
    num = input("num 1-10: ")
    cost = input("money amount: ")
    # generate a story
    story = f"""I am hungry for {food}.
I wish I had {num} of it.
But I'd need {cost} dollars!!!
"""
    print(story)
    
    
# Main Code Starts Here
create_story() #asks function to run
