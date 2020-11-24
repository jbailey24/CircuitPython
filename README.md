# CircuitPython

## Blinking LED

<img src="https://i.ibb.co/09HqdW4/IMG-5333-1.jpg" width="300">

###### <a href="https://github.com/jbailey24/CircuitPython/blob/main/LED_Blink.py">Link to the Code</a>
 In this assignment, I wired up a LED to a Metro Express and made it blink. I knew how to do this with an Arduino, but not a Metro Express, so I made my best guess on what the code would be, looked up the answer, saw how wrong I was, read the comments on the code to understand why it did what it did, and then uploaded it to the board.


## Servo

<img src="https://github.com/jbailey24/CircuitPython/blob/main/media/IMG_0873.jpg?raw=true" width="300">

###### <a href="https://github.com/jbailey24/CircuitPython/blob/main/CapTouchServo.py">Link to the Code</a>

In this assignment, I controled a servo using capacitive touch. If I touched a wire to A2, the servo would rotate one way, and if I touched a wire to A5, the servo would rotate the other way. The main problem I had with this was not really understanding how capacitive touch worked. I wrote the code for the servo and I wrote the code for capacitive touch, but I couldn't figure out how to combine the two. The reason it wasn't working was because I assigned the servo the the same pin as one of the capacitive touch pins, thinking they had to be the same. I eventually went to my dad and we worked on it together in the woods with no reception and little experience with python. We figured out how to combine the two in the end, but I used "range" to move the servo and we were both annoyed that it would go completely through 0 to 180 and then reset and wasn't able to stop at any angle besides 0 or 180. I wanted the servo to move when I was touching the pin and stop, whatever angle it was at, when I wasn't. After much trial and error we found that adding a bunch of nested if statements did the job. As an extra bonus I added a statement that told the Metro to return nothing if both wires are touched at the same time
