# Step one: user name, store in var
name = input("Enter a name: ")

# Step two: ask for $$ in CAD, store in amount_cad
# input() always gives a string.
# might need to convert to a number to do math
amount_cad = input("Enter an amount in CAD: ")
amount_cad = int(amount_cad)

# Step 3: var called amount_yen, containing our
# converted amount (1:110)
amount_yen = amount_cad * 110
amount_yen = str(amount_yen)

# Step 4: printing out the response/paragraph to user
text = "Hello, " + name + "Your new amount is "
text = text + amount_yen
print(text)






