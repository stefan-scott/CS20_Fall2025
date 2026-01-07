# Micro:bit basics
# Mr. Scott
# Jan 5, 2026
# Seeing some of micro:bit I/O

# If you get a "timed-out" or
# "could not get a prompt error"
#      press RESET on the microbit
#      re-run our program

import microbit, time

# Show Static Text
# for letter in "Centennial":
#     microbit.display.show(letter)
#     time.sleep(0.4)   #delay, measured in seconds
    
# Show Animated Text
# microbit.display.scroll("CENTENNIAL")

# -----------------------
# Micro:bit Buttons
# is_pressed() → is the button currently pressed
#                 check if it is HELD
# was_pressed() → true once per single press
#                 check for single press event

count_a = 0
count_b = 0

time.sleep(3)

# these statements reset the
# "WAS PRESSED" memory.
microbit.button_a.was_pressed()
microbit.button_b.was_pressed()

while True:
    if microbit.button_a.is_pressed():
        count_a += 1
    if microbit.button_b.was_pressed():
        count_b += 1
    print(f"a: {count_a} \t b: {count_b}")


