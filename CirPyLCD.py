import board
import time
import touchio
import math

from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

lcd = LCD(I2CPCF8574Interface(0x3f), num_rows=2, num_cols=16)

touch_left = touchio.TouchIn(board.A1)
touch_right = touchio.TouchIn(board.A4)

counter = 0
last = 0

lcd.print(str(counter))

while True:
    if touch_right.value:
        while last == 0:
            lcd.clear()
            counter = counter + 1
            lcd.print(str(counter))
            last = 1

    elif touch_left.value:
        while last == 0:
            lcd.clear()
            counter = counter - 1
            lcd.print(str(counter))
            last = 1
    else:
        last = 0
  