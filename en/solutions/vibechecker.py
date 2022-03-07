from time import sleep
from picozero import Button, RGBLED

happy = Button(3)
angry = Button(2)
sad = Button(4)
led = RGBLED(18, 17, 16)

while True:
    if happy.is_pressed:
        print('happy!')
        led.color = (255,255,0)
    elif angry.is_pressed:
        print('ANGRY!')
        led.color = (255,0,0)
    elif sad.is_pressed:
        print('sad and blue...')
        led.color = (0,125,255)
    else:
        print('throw a token in the box!')
        led.color = (0,0,0)
