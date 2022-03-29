## Code your mood lights

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
It's good practice to build your project up gradually. In this step, you will connect and code your LEDs to show different moods and test that this is working.
</div>
<div>
![A potentiometer is turned and an LED behind some paper changes colour. The paper has a face drawn on it.](images/mood-dial.gif){:width="300px"}
</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">Prototyping</span> involves making a draft of what you think your final project might achieve. The focus of prototyping is to make a simplified version of the final product quickly, to allow you to test if it is a workable solution to the problem.
</p>

A prototype that tests the connections and coded design choices will highlight any wiring or coding changes needed before the lights are embedded into a device. 

--- task ---

**Choose:** Connect your single-colour LEDs or RGB LED to the Raspberry Pi Pico:

[[[multiple-single-led-wiring]]]
[[[rgb-wiring]]]

**Tip:** If you have not already prepared your LEDs, and need to remind yourself of how to connect LEDs to resistors and jumper wires, visit our [Introduction to the Pico](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico){:target="_blank"} guide. 

--- /task ---

--- task ---

**Choose:** Import LED or RGBLED from the picozero library then set the pins for your connected LED(s):

[[[multiple-single-led-pins]]]
[[[rgb-led-pins]]]

--- /task ---

--- task ---

**Create:** Make functions for each mood that you want to use in your project. 

**Choose:** Add code within the new functions to set the LED to your chosen design for that mood.

--- collapse ---

---
title: Turn on and off multiple single-colour LEDs
---

--- code ---
---
language: python
filename: mood_indicator.py
line_numbers: false
---
def excited(): # Your first mood
    purple.on() # Turn on
    blue.off() # Turn off

def worried(): # Your second mood
    purple.off() # Turn off
    blue.on() # Turn on

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Blink or pulse multiple single-colour LED
---

Use blink or pulse to turn an LED on and off.

Blink an LED:

--- code ---
---
language: python
filename: mood_indicator.py
line_numbers: false
---

def available(): # First mood
    red.off() # Turn off the red LED
    green.blink() 


def do_not_disturb(): # First mood
    green.off() # Turn off the green LED
    red.pulse() 

--- /code ---

**Tip:** You can mix single colour, blink, and pulse effects in the same project to create the moods you want. 

--- /collapse ---

--- collapse ---

---
title: Turn on an RGB LED with a specific colour
---

--- code ---
---
language: python
filename: mood_indicator.py
line_numbers: false
---
def happy(): # Your first mood
    rgb.color = (0, 255, 0) # Your first colour

def sad(): # Your second mood
    rgb.color = (255, 0, 0) # Your second colour

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Blink, pulse, or cycle an RGB LED
---

Use `blink`, `pulse`, or `cycle` to change between colours on an RGB LED. 

--- code ---
---
language: python
filename: mood_indicator.py
line_numbers: false
---
def energise():
    rgb.blink() # Red for 1 second, green for 1 second, blue for 1 second

def neutral():
    rgb.pulse(fade_times=3) # Slow pulse
    
def relax():
    rgb.cycle(fade_times=4)
--- /code ---

--- /collapse ---

[[[generic-theory-simple-colours]]]

**Tip:** Add comments to your code next to the colour values so that you remember what colours you have created for each mood. 

--- /task ---

--- task ---

**Test:** At the end of your code, underneath your mood function definitions, add code to call your first function. 

Update your new code to call your mood functions one at a time, testing each one by running your code.

--- collapse ---

---
title: Call a mood function 
---

--- code ---
---
language: python
filename: mood_indicator.py
line_numbers: false
line_number_start: 1
line_highlights: 7
---
def happy(): # Your first mood
    rgb.color = (0, 255, 0) # Your first colour

def sad(): # Your second mood
    rgb.color = (255, 0, 0) # Your second colour

happy() # Change this line to try each of your functions

--- /code ---

--- /collapse ---

**Tip:** Make sure you new code is not indented.

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

[[[debug-pico-code]]]
[[[debug-pico-hardware]]]

--- collapse ---

---
title: My LED doesn't light when I call my mood function
---

Check that the pins in your code match the pins your LED(s) are connected to.

--- /collapse ---

--- collapse ---

---
title: My RGB LED shows the wrong colour
---

Check your code to make sure that your colour values are in the right order. Use the ['RGB colour guide'](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} to check your code matches the colour you expect.

--- /collapse ---

If you find a bug that is not listed here. Can you work out how to fix it?

We love hearing about your bugs and how you fixed them. Use the **Send feedback** button at the bottom of this page and tell us if you found a different bug in your project.

--- /task ---

