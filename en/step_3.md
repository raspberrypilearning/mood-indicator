## Code your mood lights

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
It's good practice to build your project up gradually. In this step, you will connect and code your LEDs to show different moods and test that this is working.
</div>
<div>
![A potentiometer is turned and an LED behind some paper and a face changes colour.](images/mood-dial.gif){:width="300px"}
</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">Prototyping</span> involves making a draft of what you think your final project might achieve. The focus of prototyping is to make a simplified version of the final product quickly, to allow you to test if it is a workable solution to the problem.
</p>

A prototype that tests the connections and coded design choices will highlight any wiring or coding changes needed before the lights are embedded into a device. 

--- task ---

Connect your LED(s) to the Raspberry Pi Pico:

[[[single-led-wiring]]]
[[[multiple-single-led-wiring]]]
[[[rgb-wiring]]]

**Tip:** If you have not already prepared your LEDs, and need to remind yourself of how to connect LEDs to resistors and jumper wires, visit our [Introduction to the Pico](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico){:target="_blank"} guide. 

--- /task ---

--- task ---

Import the type of LED that you are using from the picozero library:

--- collapse ---

---
title: Import the single LED 
---

--- code ---
---
language: python
filename: mood-check-in.py
line_numbers: false
---

from picozero import LED

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Import the RGB LED
---

--- code ---
---
language: python
filename: mood-check-in.py
line_numbers: false
---

from picozero import RGBLED

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

Add code to set the pins for your connected LED(s):

[[[sing-led-pins]]]
[[[multiple-single-led-pins]]]
[[[rgb-led-pins]]]

--- /task ---

--- task ---

**Create:** functions for each mood that you want to use in your project. 

Add code within the new functions to set the LED to your chosen design for that mood:

--- collapse ---

---
title: Add a function to turn on a single LED
---

--- code ---
---
language: python
filename: mood-check-in.py
line_numbers: false
---
def excited(): # Your mood
    purple.on() # Turn on

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Add functions to control multiple single LEDs
---

--- code ---
---
language: python
filename: mood-check-in.py
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
title: Blink a single colour LED
---

Use blink to turn an LED on and off.

Blink an LED:

--- code ---
---
language: python
filename: mood-check-in.py
line_numbers: false
---
led.blink() # on for 1 second then off for one second
print("Blinking") # Runs immediately

sleep(6)
led.off()
--- /code ---

Blink a fixed number of times:

--- code ---
---
language: python
line_numbers: false
---
led.blink(on_time=1, off_time=0.5)
print("Finished blinking") # Runs after 3 on/off blinks

--- /code ---

**Tip:** If you don't set off_time then it will be the same as on_time. 

--- /collapse ---

--- collapse ---

---
title: Pulse a single colour LED
---

Use `pulse` to gradually change the brightness of an LED:

--- code ---
---
language: python
filename: mood-check-in.py
line_numbers: false
---
led.pulse() # take 1 second to brighten and 1 second to dim
print("Pulsing") # Runs immediately

--- /code ---

Control the pulse speed and number of repeats:

--- code ---
---
language: python
line_numbers: false
---
led.pulse(fade_in_time=2, fade_out_time=1) # take 2 seconds to brighten and 1 second to dim
print("Finished pulsing") # Runs after 4 pulses

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Blink and pulse a single colour LED
---

You can also combine on and off times and fade in out out times to create fancy effects:

--- code ---
---
language: python
line_numbers: false
---
led.blink(on_time=1, off_time=1, fade_in_time=1, fade_out_time=1) # On for 1 second, off for 1 second, fade between
print("Fancy") # Runs immediately 
--- /code ---

**Tip:** `blink` and `pulse` will run until `off` is called or `blink` or `pulse` are called with new settings. Use `wait=True` and set `n` to blink or pulse a fixed number of times. 

--- /collapse ---

--- collapse ---

---
title: Add functions to set an RGB LED colour
---

--- code ---
---
language: python
filename: mood-check-in.py
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
title: Blink an RGB LED
---



--- /collapse ---

--- collapse ---

---
title: Pulse an RGB LED
---



--- /collapse ---

--- collapse ---

---
title: Cycle through colours on an RGB LED
---



--- /collapse ---

[[[generic-theory-simple-colours]]]

**Tip:** Add comments to your code next to the colour values so that you remember what colours you have created for each mood. 

--- /task ---

--- task ---

At the end of your code, underneath your mood function definitions, add code to call your first function. 

**Tip:** Make sure you new code is not indented.

**Test:** Run your code to test the LED(s) work as expected.

Update you new code to call your mood functions one at a time testing each one by running your code.

--- collapse ---

---
title: Call a function 
---

--- code ---
---
language: python
filename: mood-check-in.py
line_numbers: false
line_number_start: 1
line_highlights: 7
---
def happy(): # Your first mood
    rgb.color = (0, 255, 0) # Your first colour

def sad(): # Your second mood
    rgb.color = (255, 0, 0) # Your second colour

happy() 

--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

[[[debug-pico-code]]]
[[[debug-pico-hardware]]]

--- collapse ---

---
title: My LED doesn't light when I call my mood function
---

Check that the pins in your code match the pins your LED is connected to.

--- /collapse ---

--- collapse ---

---
title: My RGB LED shows the wrong colour
---

Check your code to make sure that your colour values are in the right order. Use the ['RGB Colour guide'](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} to check your code matches the colour you expect.

--- /collapse ---

If you find a bug that is not listed here. Can you work out how to fix it?

We love hearing about your bugs and how you fixed them. Use the **Send feedback** button at the bottom of this page and tell us if you found a different bug in your project.

--- /task ---

--- save ---