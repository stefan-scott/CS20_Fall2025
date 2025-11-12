# Try-Except Demo
# Mr. Scott
# Nov 12, 2025
# Try to stop our programs from crashing...so often

my_list = [88, 44, "Twenty Two"]
#           0   1       2

while True:
    try:
        index = int( input("Enter an index: ") )
        chosen_num = my_list[index]
        print("Number is: " + chosen_num)
        # if we reach this line, there
        # were no exceptions...so no need
        # to repeat!
        break
    except: #catch-all exception case
        print("Generic Error")
#     except ValueError:
#         #jumps here if we encounter a ValueError in the try: section
#         print("Value Error! Enter a number please!")
#     except IndexError:
#         print("Index Error, please enter 0, 1, or 2")
#     except TypeError:
#         print("Type Error! Please choose a string...")