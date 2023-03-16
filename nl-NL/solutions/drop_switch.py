rom time import sleep
from picozero import Button, RGBLED


happy = Button(13) # longest token
angry = Button(14) # medium token
sad = Button(15) # shortest token
led = RGBLED(18, 17, 16)


while True: # create a loop which checks for the different token
    if happy.is_pressed: # look for the longest token first
        print('happy!')
        led.color = (255,255,0) # yellow
    elif angry.is_pressed: # check for the medium token next
        print('ANGRY!')
        led.color = (255,0,0) # red
    elif sad.is_pressed: # check for the shortest token last
        print('sad and blue...')
        led.color = (0,125,255) # blue
