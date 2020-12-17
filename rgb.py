import board
import time
import digitalio

class RGB:
    def __init__(self, r, g, b):
        self.r = digitalio.DigitalInOut(r)
        self.r.direction = digitalio.Direction.OUTPUT
        
        self.g = digitalio.DigitalInOut(g)
        self.g.direction = digitalio.Direction.OUTPUT
        
        self.b = digitalio.DigitalInOut(b)
        self.b.direction = digitalio.Direction.OUTPUT
        
    def red(self):
        self.r.value = False
        self.g.value = True
        self.b.value = True
        
    def green(self):
        self.r.value = True
        self.g.value = False
        self.b.value = True
        
    def blue(self):
        self.r.value = True
        self.g.value = True
        self.b.value = False

    def cyan(self):
        self.r.value = True
        self.g.value = False
        self.b.value = False
        
    def magenta(self):
        self.r.value = False
        self.g.value = True
        self.b.value = False
        
    def yellow(self):
        self.r.value = False
        self.g.value = False
        self.b.value = True
    