import board
import time
from digitalio import DigitalInOut, Direction, Pull

#lcd setup
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)

#photointerrupter setup
phopter = DigitalInOut(board.D7)
phopter.direction = Direction.INPUT
phopter.pull = Pull.UP

start = time.time()
counter = 0
last = 0

lcd.print("Interrupts: " + str(counter))
print("The number of interrupts is: " + str(counter))

while True:
    if phopter.value == True and last == 0:
        counter = counter + 1
        last = 1
        
    if phopter.value == False:
        last = 0

    if time.time() - start > 3:
        #checks the time to see if it's been more than 4 seconds
        lcd.clear()
        lcd.print("Interrupts: " + str(counter))
        print("The number of interrupts is: " + str(counter))
        start = time.time()
        #resets time
        
  