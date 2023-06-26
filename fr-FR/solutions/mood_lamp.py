from picozero import RGBLED, Switch
from time import sleep

rgb = RGBLED(red=1, green=2, blue=3) # Numeros des broches
interrupteur = Switch(18)

option = 0

def calme():
    rgb.color = (255, 255, 0) # Jaune

def concentre():
    rgb.color = (0, 215, 0) # Orange
    
def energique():
    rgb.color = (63, 204, 208) # Vert

def choix():
    global option
    if option == 0:
        energique()
    elif option == 1:
        calme()
    elif option == 2:
        concentre()
    elif option == 3:    
        rgb.off()
    
    if option == 3:
        option = 0
    else:
        option = option + 1
    

interrupteur.when_closed = choix
