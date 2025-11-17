# More about Functions (inputs and outputs)
# Mr. Scott
# November 13, 2025
# Arguments, Parameters, Returns...
# Variable Scope: WHERE in the program a variable is accessible
#       - a variable is LOCAL to the CODE BLOCK
#         it is defined within
#
#       - if you make a variable in a function, it only
#         exists in that function!
def add_three(num1, num2, num3):
    # adds three numbers together
    # num1,2,3 → INT numbers to add
    print("global variable:", a)
    result = num1 + num2 + num3
    return result  #sends data back to the function call

# NO INDENTATION → Global Scope,
# These variables can be used anywhere
a = 99

# Two ways to use returned data
# 1.Store in a variable
# 2.Print it directly
r = add_three(5, 10, 15)
print(add_three(1,1,1))
print(add_three("b","a","d"))
