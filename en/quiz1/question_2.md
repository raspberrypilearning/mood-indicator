
--- question ---

---
legend: Question 2 of 3
---

You are trying to make an LED blink. Looking at this code, what will happen when you press the button?

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 
---

from picozero import LED, Button
from time import sleep

green = LED(13)
button = Button(18)

def success():
  green.on()
  sleep(1)
  green.off()

success()

--- /code ---

--- choices ---

- (x) Nothing will happen

  --- feedback ---
  
  That's right! The code creates a `button` variable but there's no code to do anything when the button is pressed. You could add `button.when_pressed = success`.

  --- /feedback ---

- ( ) The light will go on

  --- feedback ---
  
Try again. Read through the code and look for where the `button` appears. What does it do?

  --- /feedback ---

- ( ) The light will go off

  --- feedback ---
  
Try again. Read through the code and look for where the `button` appears. What does it do?

  --- /feedback ---

- ( ) The light will go on and off again

  --- feedback ---
  
Try again. The code *does* make the light go on and off, but read through it carefully and look for where the `button` appears. What does it do?

  --- /feedback ---

--- /choices ---

--- /question ---
