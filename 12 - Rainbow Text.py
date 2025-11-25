# Rainbow Text
# Nov 25., 2025
# Mr. Scott

from colorama import Fore, Back, Style

def rainbow_text(input_text):
    # style input_text with rainbow coloring
    # and return that styled string
    colors = [Fore.RED, Fore.YELLOW, Fore.GREEN, Fore.BLUE, Fore.MAGENTA ]
    #            0         1           2             3         4              5 OOB!!
    output_text = Style.BRIGHT + Back.BLACK
    color_index = 0
    
    for letter in input_text:
        output_text = output_text + colors[color_index]
        output_text = output_text + letter
        
        color_index += 1 #advance the color index
        if color_index >= len(colors):
            color_index = 0
    
    output_text += Back.RESET + Fore.RESET
    return output_text
    
#MAIN PROGRAM STARTS HERE
c_text = rainbow_text("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print( rainbow_text("Mr. Scott says Hi") )
print(c_text)


# non-fruitful function (no return value)
def func_a(a, b, c):
    # function that joins/prints 3 things
    # a, b, c → string type data
    print(f"{a}{b}{c}")

# fruitful functions (always return something)
def func_b(a, b, c):
    # a, b, c → string type data
    # join abc, and return the data
    return f"{a}{b}{c}"

# result = func_b("a", "b", "zzz")