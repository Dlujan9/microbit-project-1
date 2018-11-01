# Add your Python code here. E.g.
from microbit import *
import random
rock = Image("00000:"
            "09990:"
            "09990:"
            "09990:"
            "00000")

paper =Image("99999:"
            "99999:"
            "99999:"
            "99999:"
            "99999")
           
scissors =Image("99009:"
                "99090:"
                "00900:"
                "99090:"
                "99009")
             
spock = Image("99099:"
            "99099:"
            "99099:"
            "09990:"
            "09990")
         
lizard =Image("00900:"
            "09990:"
            "00900:"
            "09990:"
            "00900")
           
while True:
    if accelerometer.was_gesture("shake"):
        display.clear()
        hand = random.randint(0, 4)
        if hand == 0:
            display.show(rock)
            
        elif hand == 1:
            display.show(paper)
            
        elif hand == 2:
            display.show(scissors)
            
        elif hand == 3:
            display.show(spock)
            
        else:
            display.show(lizard)
            
        


