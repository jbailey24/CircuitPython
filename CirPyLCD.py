import board
import time
import touchio

from lcd.lcd import LCD    #importing LCD libraries 
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)

touch_left = touchio.TouchIn(board.A1)    
touch_right = touchio.TouchIn(board.A4)

counter = 0       # What is being displayed
last = 0          # Last state

lcd.print(str(counter))   #prints 0 when code is uploaded

while True:
    if touch_right.value:
        while last == 0:            #only runs if state is 0
            lcd.clear()         #clears LCD
            counter = counter + 1
            lcd.print(str(counter))
            last = 1               #sets state to 1 so that it won't keep counting

    elif touch_left.value:
        while last == 0:
            lcd.clear()
            counter = counter - 1
            lcd.print(str(counter))
            last = 1
    else:
        last = 0        #sets state to 0 when no wires are being touched
  
