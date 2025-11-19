# Reading data from Files
# Mr. Scott, Nov 19

# Make sure your file to read is in the
# same folder as your python file

# STEP ONE: open the file
my_file = open("poem.txt", "r") #r → READING

# STEP TWO: read the contents
# Option One: Read the whole file into a string
# full_text = my_file.read()
                    #usually at this point, we
                    #would split up the string somehow

# Option Two: Read each line, and store in a list
list_of_lines = my_file.readlines()

# STEP Three: Strip out the newline character for each line
for i in range(len(list_of_lines)): #0, 1, 2
    list_of_lines[i] = list_of_lines[i].rstrip("\n")
    
print(f"""A poem:
{list_of_lines[0]}
{list_of_lines[1]}
{list_of_lines[2]} """)

my_file.close()  #LAST STEP

