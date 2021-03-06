## Change your mood

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Now you need a way for the user to change moods using a button or potentiometer input. 
</div>
<div>
![A box with three emojis on the front. One is a stop sign, one is a hands up, and the other is an OK sign. Buttons next to them are pressed, which light the corresponding LED.](images/dnd-indicator.gif){:width="300px"}
</div>
</div>

--- task ---

**Find** the input components that you want to use for your mood indicator. 

You could use:
+ One button for each mood
+ A single button to move to the next mood
+ Two socket–pin jumper wires that you can connect to a crafted button or switch
+ A potentiometer to select the mood depending on the dial position

You will also need two socket–socket jumper wires for each button or three socket–socket wires for a potentiometer. 

--- /task ---

--- task ---

**Choose:** Connect your chosen input components to the Raspberry Pi Pico.

[[[single-button-wiring]]]
[[[multiple-button-wiring]]]
[[[potentiometer-wiring]]]
[[[crafted-switch-button-wiring]]]
[[[multiple-crafted-switch-button-wiring]]]

**Tip:** If you want to use components you have not used before, or need to wire some more, visit our [Introduction to the Pico](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico){:target="_blank"} guide. 

--- /task ---

--- task ---

**Choose:** Import your chosen input components from the picozero library, then create variables for the connected pins.

**Tip:** You can combine multiple imports into one line, for example `from picozero import LED, Button`.

[[[single-button-pins]]]
[[[multiple-button-pins]]]
[[[single-switch-pins]]]
[[[multiple-switches-pins]]]
[[[potentiometer-pin]]]

--- /task ---

--- task ---

**Choose:** Add code to call your mood functions based on your chosen input component. 

--- collapse ---

---
title: Change to the next mood when a single button is pressed
---

Use an `option` variable to keep track of the current mood so that you can decide which function to call next. 

Make sure the function names match the mood functions you defined in the previous step.

--- code ---
---
language: python
filename: mood_indicator.py
line_numbers: false
---
option = 0 # Store the current option

def choice(): # Call the next function and update the option
    global option
    if option == 0:
        energised() # Your first mood
    elif option == 1:
        calm()      # Your second mood
    elif option == 2:
        focused()   # Your third mood
    elif option == 3:    
        rgb.off()
    
    # Move to the next option
    if option == 3:
        option = 0
    else:
        option = option + 1
    
button.when_pressed = choice # Call the choice function when the button is pressed

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Call a different function when each button is pressed
---

You can have multiple buttons that each call a different function when they are pressed. 

Make sure you use the function names from your project and just use the name of the function, do not call it by adding brackets.

--- code ---
---
language: python
filename: mood_indicator.py
line_numbers: false
---

happy_button.when_pressed = happy
sad_button.when_pressed = sad
angry_button.when_pressed = angry

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Call a function based on the value of the potentiometer
---

If you are using a potentiometer to control outputs, then you will need to divide up the dial into equal sections. 

You can use `dial.percent` to get a value between 0 and 1 from the potentiometer. If you have five moods, then you can check whether the value is less than 20, 40, 60, 80, or 100. If you have three moods, then you can check whether the value is less than 33, 66, or 100. 

--- code ---
---
language: python
filename: mood_indicator.py
line_numbers: false
---

while True: # Loop to call a function based on the dial position
    mood = dial.percent
    print(mood)
    if mood < 20:
        happy()
    elif mood < 40:
        good()
    elif mood < 60:
        okay()
    elif mood < 80:
        unsure()
    else:
        unhappy()
    sleep(0.1) 

--- /code ---

--- /collapse ---

--- /task ---


--- task ---

**Test:** Run your script and make sure that you can switch between moods. 

--- /task ---

--- task ---

**Debug:** You might find some bugs in your project that you need to fix. Here are some common bugs.

[[[debug-pico-code]]]
[[[debug-pico-hardware]]]

If you find a bug that is not listed here. Can you work out how to fix it?

We love hearing about your bugs and how you fixed them. Use the **Send feedback** button at the bottom of this page and tell us if you found a different bug in your project.

--- /task ---

