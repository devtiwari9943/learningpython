# greating the people according to the time 
# use oof time module

import time
# get the current time 
timestamp= time.strftime('%H:%M:%S')
print(timestamp)
# extract the time 
hour = int(time.strftime('%H'))


if(hour>=0 and hour<12):
# determine the appropriate greeting
    print ("good morning sir")
elif(hour>=12 and hour <= 18):
    print("good after noon sir")
else:
    print("good evening")