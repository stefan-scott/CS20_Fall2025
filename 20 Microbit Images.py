# Micro:bit built-in images and Custom Images
# Jan 7th, 2026
# Mr. Scott

import microbit, time, random

# Display a built-in image
microbit.display.show(microbit.Image.SNAKE)
time.sleep(1)

# Display an Animation
clocks = microbit.Image.ALL_CLOCKS
ani_delay = 0.05

while True:
    for current in clocks:
        microbit.display.show(current)
        time.sleep(ani_delay)
        
        #Check for button press events
        if microbit.button_a.was_pressed():
            ani_delay = ani_delay - 0.02
            if ani_delay < 0:  # code to prevent neg
                ani_delay = 0  # values

        if microbit.button_b.was_pressed():
            ani_delay = min(0.08, ani_delay+0.02)  # max delay 0.8 seconds
            
# print(microbit.Image.STD_IMAGE_NAMES)