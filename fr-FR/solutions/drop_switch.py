from time import sleep
from picozero import Button, RGBLED


heureux = Button(13) # Jeton le plus long
colere = Button(14) # Jeton moyen
triste = Button(15) # Jeton le plus court
led = RGBLED(18, 17, 16)


while True: # Creer une boucle qui verifie les differents jetons
    if heureux.is_pressed: # Cherche d'abord le jeton le plus long
        print('heureux!')
        led.color = (255,255,0) # Jaune
    elif colere.is_pressed: # Cherche ensuite le jeton moyen
        print('EN COLERE!')
        led.color = (255,0,0) # Rouge
    elif triste.is_pressed: # Recherche le jeton le plus court en dernier lieu
        print('triste et bleu...')
        led.color = (0,125,255) # Bleu
