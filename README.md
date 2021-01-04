# CircuitPython

## Blinking LED

<img src="https://i.ibb.co/09HqdW4/IMG-5333-1.jpg" width="300">

###### <a href="https://github.com/jbailey24/CircuitPython/blob/main/LED_Blink.py">Link to the Code</a>
 In this assignment, I wired up a LED to a Metro Express and made it blink. I knew how to do this with an Arduino, but not a Metro Express, so I made my best guess on what the code would be, looked up the answer, saw how wrong I was, read the comments on the code to understand why it did what it did, and then uploaded it to the board.


## Servo

<img src="https://github.com/jbailey24/CircuitPython/blob/main/media/IMG_0873.jpg?raw=true" width="300">

###### <a href="https://github.com/jbailey24/CircuitPython/blob/main/CapTouchServo.py">Link to the Code</a>

In this assignment, I controled a servo using capacitive touch. If I touched a wire to A2, the servo would rotate one way, and if I touched a wire to A5, the servo would rotate the other way. The main problem I had with this was not really understanding how capacitive touch worked. I wrote the code for the servo and I wrote the code for capacitive touch, but I couldn't figure out how to combine the two. The reason it wasn't working was because I assigned the servo the the same pin as one of the capacitive touch pins, thinking they had to be the same. I eventually went to my dad and we worked on it together in the woods with no reception and little experience with python. We figured out how to combine the two in the end, but I used "range" to move the servo and we were both annoyed that it would go completely through 0 to 180 and then reset and wasn't able to stop at any angle besides 0 or 180. I wanted the servo to move when I was touching the pin and stop, whatever angle it was at, when I wasn't. After much trial and error we found that adding a bunch of nested if statements did the job. As an extra bonus I added a statement that told the Metro to return nothing if both wires are touched at the same time


## LCD

<img src="https://github.com/jbailey24/CircuitPython/blob/main/media/IMG_5584.GIF?raw=true" width="350"><img src="https://github.com/jbailey24/CircuitPython/blob/main/media/IMG_0917.jpg?raw=true" width="200">

###### <a href="https://github.com/jbailey24/CircuitPython/blob/main/CirPyLCD.py">Link to the Code</a>

In this assignment, I used my knowledge of capacitive touch and LCDs to control a counter displayed on a LCD. If I touched a wire to A4 the counter went up and if I touched a wire to A1 the counter went down. Getting all the libraries set up actully went fairly smoothly for me. I had to find a "real" computer (not chromebook) to update my Metro Express, but once I did that, I didn't have any problems. To ensure the counter only went up/down one when the wire was touched (instead of going up/down continually), I added a variable for the last state it was in. When the wire was removed, it would return a state of 0, whereas if it was touching the pin it would return a state of 1. The counting code would only run if the previous return was 0. I also had trouble with printing integers to my LCD. In the end, I ended up just using str() to turn the counter variable into a string. 

NOTE: I just realized while writing this description that I forgot to include a count direction on my LCD. It's a small enough thing I'm not going to go back and add it at this point, but I feel like I should acknowledge that I left it out. 

## Photointerrupter

<img src="https://github.com/jbailey24/CircuitPython/blob/main/media/IMG_0922.jpg?raw=true" width="200">

###### <a href="https://github.com/jbailey24/CircuitPython/blob/main/Photointerrupter.py">Link to the Code</a>

In this assignment, I measured the number of times a photointerrupter was interrupted and displayed it on an lcd. I was delighted to find that I didn't encounter any problems getting it to work. Thanks to the lovely people on the internet, I was able to figure out how to "pull up" the digital pin and write a delay without using sleep(). Adding the lcd was super easy and took about two seconds because I could just borrow from the previous assignment. 

## Distance Sensor

###### <a href="https://github.com/jbailey24/CircuitPython/blob/main/Distance.py">Link to the Code</a>

In this assignment, I used an ultrasonic distance sensor to measure distance and the buit-in Metro Express neopixel to display a coresponding color according to the scale below.

<p align="center">
  <img src="https://github.com/jbailey24/CircuitPython/blob/main/media/color%20spectrum%20(1).png?raw=true" width="400">
</p>

Ultrasonic sensors work by sending out ultrasonic waves, which bounce off of nearby objects back towards the sensor. The sensor receives the waves and is able to calculate the distance based on the time between when the signal was sent and received. To simplify things, <a href="https://github.com/adafruit/Adafruit_CircuitPython_HCSR04/blob/master/adafruit_hcsr04.py">this library</a> does the math for you, so all that I needed was ` sonar.distance` to measure the distance.
<br>
<br>
More difficult was the neopixel. One way to achieve the rainbow effect would be to use if statments to assign a range of distances per one color, but this would look choppy as there would only be a few set colors, and not to mention there would be lots of uneccesary code. A more ideal way would be to have, for any input value, a unique output color value. Color value is assigned based on the amounts of red (r), green (g), and blue (b), each measured on a scale from 0 to 255, so this can be done by using a formula which solves for a value of r, g, or b based on the input and stringing the values together. This does mean that I needed to find those formulas though. 
<br>
<br>
To get a general idea of what each equation would look like, I thought about the values of the color as the distance increased from 5 to 35. Red would start out at 255 and slowly fade so that by 20 it equalled 0. Green would start at 0, begin to rise at 20, and reach 255 at 35. Blue would start a 0, rise until at 20 it was 255, and then fall so that by 35 it was again 0. In short, When graphed, they would be curves with different means. For the curve formula, I first tried the Gaussian function which looks like this:

<p align="center">
  <img src="https://github.com/jbailey24/CircuitPython/blob/main/media/maxresdefault.jpg?raw=true" width="300"><img src="https://github.com/jbailey24/CircuitPython/blob/main/media/Screenshot%202020-12-07%20at%204.35.56%20PM.png?raw=true" width="200">
 </p>
But I decided to change it around some, so it looked like this:

<p align="center">
  <img src="https://github.com/jbailey24/CircuitPython/blob/main/media/Screenshot%202020-12-07%20at%204.36.31%20PM.png?raw=true" width="190">                           </p>                                                                                                        
                                                                                                                                         
because the plateau would let the color linger longer on the primary colors. The means for the equations were 5 for red, 35 for green, and 20 for blue, but I still needed to find the standard deviation. Knowing that the distance between 255 and (approximately) 0 should be 15, I found that 7.75 worked best. The last variable that I needed to find was the multiplier. To have the proper outputs, the maximum y value had to be 255, but without the multiplier, it was much lower. I found it by setting the equation equal to 255 when x equaled the mean and solved for a, which turned out to be 1976.25. And so, the final equations looked like this:

<p align="center">
  <img src="https://github.com/jbailey24/CircuitPython/blob/main/media/canvas.png?raw=true" width="200"><img src="https://github.com/jbailey24/CircuitPython/blob/main/media/Screenshot%202020-12-07%20at%203.35.29%20PM.png?raw=true" width="300">
</p> 
To see the full range of colors run <a href="https://github.com/jbailey24/CircuitPython/blob/main/Rainbow.py">this code</a>. Because these equations only work from 5 to 35, outside of that range the neopixel is either soild red or green. While I didn't find the actual distance sensor part of the assignment too difficult, getting the neopixel to work was very rewarding and this was overall a very enjoyable challenge.


## Classes, Objects, and Modules

###### <a href="https://github.com/jbailey24/CircuitPython/blob/main/rgb.py">Link to Library</a>
###### <a href="https://github.com/jbailey24/CircuitPython/blob/main/rgbRun.py">Link to Code</a>

<p align="center">
<img src="https://github.com/jbailey24/CircuitPython/blob/main/media/IMG_0956.jpg?raw=true" width="300">
</p>

In this assignmnet, I created a library for rgb led colors. Instead of assigning color values in your main code, with the library you can reference the library and just call the color name. The assignment wasn't too difficult, but learning about the aplication of classes and modules was interesting. I found the dog example in the assignment description very helpful, so I'm going to put it in here for when I inevitably forget how to do this, and come looking to this page for answers.
```
class Dog:
     kind = "canine"
 
     def __init__(self, breed, age):
          self.breed = breed 
          self.age = age
          self.tricks = []

     def addTrick(self, trick):
          self.tricks.append(trick)

     def bark(self):
          return "arf"
```
```
from dog import Dog

Rex = Dog("Golden", 8)      
Spot = Dog("Pit Bull", 12)  
Rex.addTrick("roll over")  
Spot.addTrick("sit")       
Spot.addTrick("play dead") 

print(Rex.kind)         
print(Spot.kind)
print(Rex.breed)         
print(Rex.age)    
print(Spot.breed)
print(Spot.age)
print(Rex.tricks)       
print(Spot.tricks)

Spot.age += 1              
Spot.weight = 70            # this is bad form.

print(Spot.age)            
print(Spot.weight)          # you're allowed to do this, but ew.
print(Spot.bark())  
```

## Fancy LED

<p align="center">
<img src="https://github.com/jbailey24/CircuitPython/blob/main/media/IMG_0966.jpg?raw=true" width="300">
</p>

###### <a href="https://github.com/jbailey24/CircuitPython/blob/main/fancyLED.py">Link to Library</a> 
###### <a href="https://github.com/jbailey24/CircuitPython/blob/main/fancyLEDrun.py">Link to Code</a>

In this assignment, I created a library that defines four different sequences of flashing among a group of three LEDs. The goal was to create the library in a way such that <a href="https://github.com/jbailey24/CircuitPython/blob/main/fancyLEDrun.py">this code</a> would work. The four sequences were `alternate()`, `blink()`, `chase()`, and `sparkle()`. After doing the previous assignment, I was well equipted to do this one. The biggest challenge I faced was finding a way to be more concise in my code. The defining all of these sequences was very repetitive and long. So, in the library, I defined `off()`, which set all of the LEDs to off, and `on()`, which set all of the LEDs to on. 

