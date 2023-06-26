from picozero import LED, Speaker, Button
from time import sleep

manger = LED(13)
boire = LED(8)
jouer = LED(5)

haut_parleur = Speaker(1)

choisir = Button(18)
confirmer = Button(22)

option = 0 # Memorise l'option actuelle

def choix(): # Appelle la fonction suivante et mets a jour l'option
    global option
    if option == 0:
        manger.on()
        boire.off()
        jouer.off()
    elif option == 1:
        manger.off()
        boire.on()
        jouer.off()    
    elif option == 2:
        manger.off()
        boire.off()
        jouer.on()   
    elif option == 3:
        manger.off()
        boire.off()
        jouer.off()

    if option == 3:
        option = 0
    else:
        option = option + 1

def son_buzzer():
    haut_parleur.on()
    sleep(1)
    haut_parleur.off()

choisir.when_pressed = choix 
confirmer.when_pressed = son_buzzer
