## Change your mood

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Now you need a way for the user to change moods using button or potentiometer inputs. 
</div>
<div>
![](images/image.png){:width="300px"}
</div>
</div>

--- task ---

**Find** the input components that you want to use for your mood check-in. 

You could use:
+ One button for each mood
+ A single button to move to the next mood
+ A potentiometer to select the mood depending on the dial position

You will also need two socket-socket jumper wires for each button or three socket-to-socket wires for a potentiometer. 

--- /task ---

--- task ---

Connect your input components to the Raspberry Pi Pico

single-button-wiring
multiple-button-wiring
potentiometer-wiring

**Tip:** If you want to use components you have not used before, or need to wire some more, visit our [Introduction to the Pico](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico){:target="_blank"} guide. 

--- /task ---

--- task ---

Import the Python library for the type of input component you are using:

**Tip:** You can combine multiple imports into one line, for example `from picozero import LED, Button`.

--- collapse ---

---
title: Import the library used by a button
---

--- code ---
---
language: python
filename: mood-check-in.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---

from picozero import Button

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Import the library used by a potentiometer
---

--- code ---
---
language: python
filename: mood-check-in.py
line_numbers: false
line_number_start: 1
line_highlights: 1
---

from picozero import Pot

--- /code ---

--- /collapse ---

--- task ---

Create a variable for each input component using the pin that you have connected it to:

single button pins ingredient
mulitple button LEDs pin ingredient
potentiometer pins ingredient

--- /task ---

Now you need to add code to call your mood functions based on the input. 

--- task ---

--- collapse ---

---
title: Call a different function when each button is pressed
---

--- code ---
---
language: python
filename: mood-check-in.py
line_numbers: true
line_number_start: 
line_highlights: 
---

happy_button.when_pressed = happy
sad_button.when_pressed = sad
angry_button.when_pressed = angry

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Switch to the next mood when a single button is pressed
---

--- code ---
---
language: python
filename: mood-check-in.py
line_numbers: true
line_number_start: 
line_highlights: 
---



--- /code ---

--- /collapse ---

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

--- collapse ---

---
title: 
---



--- /collapse ---

If you find a bug that is not listed here. Can you work out how to fix it?

We love hearing about your bugs and how you fixed them. Use the **Send feedback** button at the bottom of this page and tell us if you found a different bug in your project.

--- /task ---

--- save ---