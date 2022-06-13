from picozero import RGBLED, Switch
from time import sleep

rgb = RGBLED(red=1, green=2, blue=3) # pin numbers
switch = Switch(18)

option = 0

def calm():
    rgb.color = (255, 255, 0) # yellow

def focused():
    rgb.color = (0, 215, 0) # orange
    
def energised():
    rgb.color = (63, 204, 208) # green

def choice():
    global option
    if option == 0:
        energised()
    elif option == 1:
        calm()
    elif option == 2:
        focused()
    elif option == 3:    
        rgb.off()
    
    if option == 3:
        option = 0
    else:
        option = option + 1
    

switch.when_closed = choice