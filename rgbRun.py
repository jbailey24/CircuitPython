import time
import board
from rgb import RGB

r1 = board.D3
g1 = board.D4
b1 = board.D5
r2 = board.D8
g2 = board.D9
b2 = board.D10

myRGB1 = RGB(r1,g1,b1)
myRGB2 = RGB(r2,g2,b2)

myRGB1.red()
myRGB2.green()
time.sleep(1)
myRGB1.blue()
myRGB2.cyan()
time.sleep(1)
myRGB1.magenta()
myRGB2.yellow()
time.sleep(1)

