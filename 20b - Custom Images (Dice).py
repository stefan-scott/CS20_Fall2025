# Custom Images - Dice
# Jan 7 2026
# Mr. Scott

import microbit, time, random
# LED Values 0-off    9-full brightness

# create an image of a die with a one
dice4 = "33333:39093:30003:39093:33333"
dice4 = microbit.Image(dice4)

dice1 = "33333:30003:30903:30003:33333"
dice1 = microbit.Image(dice1)

dice3 = "33333:" \
        "30093:" \
        "30903:" \
        "39003:" \
        "33333"
dice3 = microbit.Image(dice3)

#USING THE DICE, LET'S MAKE A GAME..."
dice_images = [dice1, dice3, dice4]
dice_values = [1,     3,     4]
#              0      1      2
user_total = 0

while True: # game loop
    #A Button - roll the die
    if microbit.button_a.was_pressed():
        index = random.randrange(0,len(dice_images))
        microbit.display.show(dice_images[index])
        user_total += dice_values[index]
        print(user_total)
        
        #Goal - get close to 21 without going over
        if user_total > 21:
            print("OVER - you lose")
            time.sleep(1)
            microbit.display.show(microbit.Image.SKULL)
            break
        elif user_total == 21:
            print("21 - You win!")
            time.sleep(1)
            microbit.display.show(microbit.Image.HAPPY)
            break
