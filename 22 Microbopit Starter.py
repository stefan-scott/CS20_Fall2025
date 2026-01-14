# Micro:bopit Starter
# + shake detection

import random, time, microbit

def is_shaking():
    # Boolean Function: return True or False
    # depending on if the microbit is presently shaking
    min_z = microbit.accelerometer.get_z()
    max_z = min_z
    
    #use a loop to sample the z_accel 10 times
    for i in range(10):
        z = microbit.accelerometer.get_z()
        min_z = min(min_z, z)
        max_z = max(max_z, z)
        
    # determine difference between max_z and min_z
    total_diff = abs(max_z - min_z)
    
    #1000 is the "sensitivity"...can adjust as needed
    if total_diff > 1000:
        return True
    else:
        return False
        
        
while True:
    if is_shaking():
        print("Shaking")
    else:
        print("not shaking")
