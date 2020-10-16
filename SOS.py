import board
import neopixel
import time

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)


#It's not neatly written, but I don't want to get too indepth on a short assignment 

while True:
    print("SOS")
    dot.fill((0,0,0))
    time.sleep(1.5)
    dot.fill((250,0,0))
    time.sleep(.25)
    dot.fill((0,0,0))
    time.sleep(.075)
    dot.fill((250,0,0))
    time.sleep(.25)
    dot.fill((0,0,0))
    time.sleep(.075)
    dot.fill((250,0,0))
    time.sleep(.25)
    dot.fill((0,0,0))
    time.sleep(.40)
    dot.fill((250,0,0))
    time.sleep(.5)
    dot.fill((0,0,0))
    time.sleep(.1)
    dot.fill((250,0,0))
    time.sleep(.5)
    dot.fill((0,0,0))
    time.sleep(.1)
    dot.fill((250,0,0))
    time.sleep(.5)
    dot.fill((0,0,0))
    time.sleep(.40)
    dot.fill((250,0,0))
    time.sleep(.25)
    dot.fill((0,0,0))
    time.sleep(.075)
    dot.fill((250,0,0))
    time.sleep(.25)
    dot.fill((0,0,0))
    time.sleep(.075)
    dot.fill((250,0,0))
    time.sleep(.25)
