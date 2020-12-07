import neopixel
import time
import board
import math

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)

while True:
    
    dot.fill((255, 0, 0))
    print(255.0, ",", 0.0, ",", 0.0)
    time.sleep(0.2)
    
    for x in range(5,35,1):
        r = (2*988.125)*((1/(7.75))*((math.e)**(-((x)-5)**(4)/(2*(7.75)**4))))
        g = (2*988.125)*((1/(7.75))*((math.e)**(-((x)-35)**(4)/(2*(7.75)**4))))
        b = (2*988.125)*((1/(7.75))*((math.e)**(-((x)-20)**(4)/(2*(7.75)**4))))
    
        dot.fill(((round(r)),(round(g)),(round(b))))
        
        print(round(r,1), ",", round(g,1), ",", round(b,1))
        time.sleep(.2)
        
    dot.fill((0, 255, 0))
    print(0.0, ",", 255.0, ",", 0.0)
    time.sleep(0.2)
    
    for x in range(35,5,-1):
        r = (2*988.125)*((1/(7.75))*((math.e)**(-((x)-5)**(4)/(2*(7.75)**4))))
        g = (2*988.125)*((1/(7.75))*((math.e)**(-((x)-35)**(4)/(2*(7.75)**4))))
        b = (2*988.125)*((1/(7.75))*((math.e)**(-((x)-20)**(4)/(2*(7.75)**4))))
    
        dot.fill(((round(r)),(round(g)),(round(b))))
        
        print(round(r,1), ",", round(g,1), ",", round(b,1))
        time.sleep(.2)
        
