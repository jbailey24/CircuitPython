import board
import time
from lib import UltraSonic
    # The Ultrasonic Distance Sensor library
import neopixel
import math

sonar = UltraSonic.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)
    # Assigns the trigger and echo pins

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
    # Assigns neopixel on board

while True:
    try:
        # Try/except keeps the code running when there are frequent errors, as is the case with ultrasonic sensors
        # (errors occur when the sensor sends a ping out and doesn't receive one back because there is nothing in range to bouce 
        # off of or the object is at an angle). The 'try' tells it to try running the indented code and then run the code
        # under 'execpt' if it receives an error. Code under 'else' is run regardless of whether an error is recieved or not
        
        print(round(sonar.distance, 1))
        x = sonar.distance
            # By assigning 'x' in the 'try' block, it prevents the code from stopping for errors resulting 
            # from outlying distance readings
            
    except RuntimeError:
        # If an error is received, it will print 'Retrying!' to the serial monitor
        print("Retrying!")
        pass
 
    else:
        if 5 <= x <= 35:
            r = (2*988.125)*((1/(7.75))*((math.e)**(-((x)-5)**(4)/(2*(7.75)**4))))
            g = (2*988.125)*((1/(7.75))*((math.e)**(-((x)-35)**(4)/(2*(7.75)**4))))
            b = (2*988.125)*((1/(7.75))*((math.e)**(-((x)-20)**(4)/(2*(7.75)**4))))
                # This is the equation for a curve (with a unique mean for each variable). For any given 'x' value in the range
                # 5 < x < 35, it will find a corresponding y value ranging from 0 to 255. The values are plugged into rgb format
                # and together constitute a color. The curves are such that as the red curve has a negative slope, the blue
                # curve has a positive one, and as the blue has a negative slope, green has positive. This ensures smooth
                # transitioning between colors and a rainbow-like effect when increasing 'x' values are consecutively entered.
                
            dot.fill(((round(r)),(round(g)),(round(b))))
 
        elif x < 5:
            # If 'x' is not in the range 5-35, the neopixel will fill either true red or true green accordingly
            dot.fill((255,0,0))
        elif 35 < x:
            dot.fill((0,255,0))
            
    time.sleep(0.1)
        # The code runs every 0.1 of a second 
    
            
