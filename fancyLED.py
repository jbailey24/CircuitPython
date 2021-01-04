import board
import time
import digitalio

x = 0
y = 0
z = 0
banana = 0

class FancyLED:
    def __init__(self, led1, led2, led3):
        self.led1 = digitalio.DigitalInOut(led1)
        self.led1.direction = digitalio.Direction.OUTPUT
        
        self.led2 = digitalio.DigitalInOut(led2)
        self.led2.direction = digitalio.Direction.OUTPUT
        
        self.led3 = digitalio.DigitalInOut(led3)
        self.led3.direction = digitalio.Direction.OUTPUT
    
    def off(self):
        self.led1.value = False
        self.led2.value = False
        self.led3.value = False
    
    def on(self):
        self.led1.value = True
        self.led2.value = True
        self.led3.value = True
        
        
    def alternate(self):
        for x in range(0, 3):
            self.led1.value = True
            self.led2.value = False
            self.led3.value = True
            time.sleep(.727272)
            self.led1.value = False
            self.led2.value = True
            self.led3.value = False
            time.sleep(.727272)
            x += 1
            
        self.off()
        
            
    def blink(self):
        for y in range(0, 6):
            self.on()
            time.sleep(0.363636)
            self.off()
            time.sleep(0.363636)
            y += y
            
        self.off()
        
        
    def chase(self):
        for z in range (0, 6):
            self.led1.value = False
            self.led2.value = False
            self.led3.value = True
            time.sleep(0.181818)
            self.led1.value = False
            self.led2.value = True
            self.led3.value = False
            time.sleep(0.181818)
            self.led1.value = True
            self.led2.value = False
            self.led3.value = False
            time.sleep(0.181818)
            self.off()
            time.sleep(0.363636)
            z += z
            
        self.off()
        
    def sparkle(self):
        for banana in range (0,6):
            self.led1.value = True
            self.led2.value = False
            self.led3.value = False
            time.sleep(0.090909)
            self.led1.value = False
            self.led2.value = True
            self.led3.value = True
            time.sleep(0.090909)
            self.led1.value = True
            self.led2.value = False
            self.led3.value = True
            time.sleep(0.090909)
            self.led1.value = True
            self.led2.value = True
            self.led3.value = False
            time.sleep(0.090909)
            self.led1.value = False
            self.led2.value = False
            self.led3.value = True
            time.sleep(0.090909)
            self.led1.value = False
            self.led2.value = True
            self.led3.value = False
            time.sleep(0.090909)
            banana += banana
        
        self.off()
            
        