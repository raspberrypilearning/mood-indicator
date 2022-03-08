from picozero import LED, Speaker, Button
from time import sleep

eat = LED(13)
drink = LED(8)
play = LED(5)

speaker = Speaker(1)

choose = Button(18)
confirm = Button(22)

option = 0 # store the current option

def choice(): # call the next function and update the option
    global option
    if option == 0:
        eat.on()
        drink.off()
        play.off()
    elif option == 1:
        eat.off()
        drink.on()
        play.off()    
    elif option == 2:
        eat.off()
        drink.off()
        play.on()   
    elif option == 3:
        eat.off()
        drink.off()
        play.off()

    if option == 3:
        option = 0
    else:
        option = option + 1

def sound_buzzer():
    speaker.on()
    sleep(1)
    speaker.off()

choose.when_pressed = choice 
confirm.when_pressed = sound_buzzer