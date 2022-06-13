from picozero import RGBLED, Pot
from time import sleep

rgb = RGBLED(red=1, green=2, blue=3)
dial = Pot(0)

def happy():
    rgb.color = (0, 255, 0) # green
    
def good():
    rgb.color = (75, 255, 0) # yellow-green

def okay():
    rgb.color = (255, 150, 0) # yellow
    
def unsure():
    rgb.color = (255, 25, 0) # orange

def unhappy():
    rgb.color = (255, 0, 0) # red
    

while True:
    mood = dial.percent
    print(mood)
    if mood < 20:
        happy()
    elif mood < 40:
        good()
    elif mood < 60:
        okay()
    elif mood< 80:
        unsure()
    else:
        unhappy()
    sleep(0.1)
