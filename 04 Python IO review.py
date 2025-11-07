# Python O Review
# Mr. Scott
# November 7, 2025
# Input and printing multiple things....

# OUTPUT (lvl 1) - printing one piece of data
print(99)       # print a number
print("hello")  # print a string literal
text = "CS20"
print(text)     # print a variable (contains a string)

# OUTPUT (lvl 2) - printing multiple strings at once
print("hello" + text)  #STR + STR  → join/concatenation
print("hello", text, 99) #print with , → 2 or more thing, adds a space

# OUTPUT (lvl 3) - printing mixed types
num = 45
#           STR       +     INT
print("best number: " + str(num))
print("best number:", num)

# OUTPUT (lvl Max) - formatted strings
# escape sequences:  \t → tab   \n → newline
new_text = f"best number: {num}\nText: {text} "
print(new_text)





