import board
import time
from lib import UltraSonic
import neopixel
import math

sonar = UltraSonic.HCSR04(trigger_pin=board.D5, echo_pin=board.D6)

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    try:
        print(round(sonar.distance, 1))
        x = sonar.distance
    except RuntimeError:
        print("Retrying!")
        pass
    else:
        if 5 <= x <= 35:
            r = (2*988.125)*((1/(7.75))*((math.e)**(-((x)-5)**(4)/(2*(7.75)**4))))
            g = (2*988.125)*((1/(7.75))*((math.e)**(-((x)-35)**(4)/(2*(7.75)**4))))
            b = (2*988.125)*((1/(7.75))*((math.e)**(-((x)-20)**(4)/(2*(7.75)**4))))
    
            dot.fill(((round(r)),(round(g)),(round(b))))
 
        elif x < 5:
            dot.fill((255,0,0))
        elif 35 < x:
            dot.fill((0,255,0))
    time.sleep(0.1)
    
            