# Styling Text in Python
# Mr. Scott
# November 24, 2025
# Also, seeing how to use/install new libraries

# two NEW libraries: colorama emoji
# install:  tools→manage packages

import emoji
from colorama import Fore, Back, Style

# testing the emoji library
print(emoji.emojize("Testing an emoji :thumbs_up:"))
print(emoji.emojize(":Santa_Claus:  :deer: :T-Rex:  :ZZZ:  ")) #add 3-4 emojis

# testing text color and style (colorama)
# Fore → Text color   Back→Highlight color
# Style → Change weight of text
print(Fore.RED + "Red" + Fore.BLUE + "Blue" + Fore.RESET)
print(Back.YELLOW + "Yellow" + Back.MAGENTA + "Magenta" + Back.RESET)
print(Fore.GREEN +  Style.DIM + "Dim" + Style.BRIGHT + "Bright" + Style.NORMAL + "Normal")





