import board
import time
import touchio
import pulseio
from lib import servo
import neopixel

touch_left = touchio.TouchIn(board.A2)
touch_right = touchio.TouchIn(board.A5)

dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
pwm = pulseio.PWMOut(board.A3, duty_cycle=2 ** 15, frequency=50)

myServo = servo.Servo(pwm)

print("on")
angle = 90

while True:
    if touch_right.value:
        if touch_left.value:
            print("Nothing touched")
            dot.fill((0,250,0))
            time.sleep(0.05)
        else:
            print("right touched!")
            dot.fill((250,0,0))
            if angle < 180:
                myServo.angle = angle
                angle = angle + 2
    elif touch_left.value:
        if touch_right.value:
            print("Nothing touched")
            dot.fill((0,250,0))
            time.sleep(0.05)
        else:
            print("left touched!")
            dot.fill((0,0,250))
            if angle > 0:
                myServo.angle = angle
                angle = angle - 2
    else:
        print("Nothing touched")
        dot.fill((0,250,0))
        time.sleep(0.05)