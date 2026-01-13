# Microbit Image Functions
# Mr .Scott
# January 8, 2026

import microbit, time, random

# grid[3][4]
# grid[y][x]


# ----------------------------------
#    LED Library CODE         
# ----------------------------------

grid = [ [0, 0, 0, 0, 0 ],
         [0, 0, 0, 0, 0 ],
         [0, 0, 0, 0, 0 ],
         [0, 0, 0, 0, 0 ],
         [0, 0, 0, 0, 0 ] ]

def print_grid():
    #print out the grid in an easy-to-read format
    for row in grid:
        print(row)

def show_grid():
    #convert our 2D list to a string, and display
    result = ""
    for row in grid:
        for pixel in row:
            result += str(pixel)
        result += ":"
        
    result = result[0:-1]
#     print(result)
    microbit.display.show(microbit.Image(result))

def set_pixel(x, y, intensity):
    #set a pixel at (x,y) to a brightness (0-9)
    grid[y][x] = intensity
    show_grid()

def plot(x,y):
    #pixel at (x,y) to full brightness
    set_pixel(x,y,9)

def unplot(x,y):
    #turn off led at (x,y)
    set_pixel(x,y,0)

def queue_pixel(x, y, intensity):
    #modify a pixel, but don't display yet...
    grid[y][x] = intensity

def set_all(intensity):
    # intensity → INTEGER representing brightness (0-9)
    # turn on all LEDs
    for x in range(5):      #0, 1, 2, 3, 4
        for y in range(5):  #0, 1, 2, 3, 4
            queue_pixel(x,y,intensity)
    show_grid()
    
# ------------------------------------------------------
#                   Library Ends Here
# ------------------------------------------------------

# Fading Screen Animation
# 0 1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
for i in range(5):
    for brightness in range(10):
        set_all(brightness)
        time.sleep(0.005)

    for brightness in range(8, 0, -1):
        set_all(brightness)
        time.sleep(0.005)
set_all(0)


# ----- START Sprite Game Here ---------------

def generate_item_x():
    #returns an x-position for new item (0,1,2,3,4)
    #ensures it doesn't line up with player
    x = random.randrange(0,5)
    while x == player_x:
        x = random.randrange(0,5)
    return x

#---- SETUP CODE ----
player_x = 2
player_y = 4

item_x = generate_item_x()
item_y = 0
queue_pixel(item_x, item_y, 5)

start_time = time.time()
# time.time() returns seconds since
# January 1, 1970, midnight
# GMT -0


plot(player_x, player_y)

# ---- MAIN LOOP -----
while True:
    queue_pixel(player_x, player_y, 0)
    
    # Check for user event:
    if microbit.button_a.was_pressed():
        player_x -= 1
        if player_x < 0:
            player_x = 0
    
    if microbit.button_b.was_pressed():
        player_x = min(player_x + 1, 4)
     
     
    #Timer Code
    elapsed_time = time.time() - start_time
    print(elapsed_time)
    
    #check for 1 second elapsed:
    if elapsed_time > 0.4:
        print("One Second Elapsed")
        start_time = time.time() #reset timer
        
        #drop item, and also check for "catching"
        queue_pixel(item_x, item_y,0)
        item_y += 1
        
        if item_y == 4: #reached the bottom
            if item_x == player_x:
                print("ITEM CAUGHT")
            else:
                print("ITEM MISSED")
            item_y = 0
            item_x = generate_item_x()
            
         
        
     
    
    plot(player_x, player_y)
    time.sleep(0.1)

