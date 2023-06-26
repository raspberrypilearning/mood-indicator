## Ce que tu vas faire

Créer un dispositif d'enregistrement d'humeur avec des lumières colorées pour exprimer ton humeur actuelle.

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
Prêter attention à ton humeur actuelle est une manière de favoriser ton bien-être. C'est <span style="color: #0faeb0">normal</span> de se sentir en colère ou triste, tout comme il est <span style="color: #0faeb0">normal</span> de se sentir heureux ou excité. Un <span style="color: #0faeb0">enregistrement d'humeur</span> est un moment où tu remarques ce que tu ressens et où tu l'enregistres ou le fais savoir aux autres. 
</p>

Tu vas devoir :
+ **Représenter** des humeurs ou des émotions à l'aide de lumières colorées
+ Développer des contrôles d'entrée pour ton appareil afin de permettre à l'utilisateur **d'enregistrer** son humeur
+ Coder des LED(s) pour créer **des effets de lumière** basés sur différentes humeurs

Pour mener à bien ce projet, tu auras besoin de :

**Matériel**

Tu peux acheter tout le matériel requis pour ce projet et les autres projets du parcours à partir de la [boutique en ligne Pimoroni](https://shop.pimoroni.com/products/pico-intro-kit?variant=39893512945747){:target='_blank'} et [boutique en ligne Kitronik](https://kitronik.co.uk/products/5343-raspberry-pi-foundation-pico-pathway-pack){:target='_blank'}

+ Un Raspberry Pi Pico avec des broches soudées dessus
+ Un câble de données USB A vers micro USB
+ Des LED(s) RVB **à Cathode commune** ou des LED(s) monochrome(s)
+ Un potentiomètre ou des boutons (achetés ou fabriqués)
+ Fils de liaison
+ Des résistances
+ Matériaux de bricolage, dont carte, ruban adhésif et papier d'aluminium

**Logiciel:**
+ Thonny : ce projet peut être réalisé à l'aide de l'éditeur Thonny Python, qui peut être installé sur un ordinateur Linux, Windows ou Mac.

[[[thonny-install]]]

[[[change-theme-thonny]]]

+ picozero - tu devras configurer picozero sur ton Raspberry Pi Pico

[[[set-up-picozero]]]

--- task ---

**Regarde :** Jette un coup d'œil à cet indicateur d'humeur. Comment utilise-t-il les couleurs pour indiquer une humeur ? Comment changes-tu la couleur affichée ?

![Un morceau de papier calque est enroulé autour d'un gobelet en carton. Une LED RVB se trouve à l'intérieur, qui éclaire le papier calque de différentes couleurs en fonction du nombre de fois que le bouton a été enfoncé.](images/mood-lamp.gif)

--- collapse ---
---
title: Voir à l'intérieur
---
--- code ---
---
language: python
filename: mood_lamp.py
line_numbers: true
line_number_start: 1
line_highlights: 
---
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
--- /code ---

--- /collapse ---

--- /task ---

--- no-print ---

## Trouve l'inspiration 💭

Explore ces exemples de projets pour obtenir plus d'idées .

**Interrupteur de chute** Des jetons de différentes tailles sont enveloppés dans du papier d'aluminium avec des humeurs écrites dessus. Lorsqu'ils sont placés dans la boîte, ils ferment différents interrupteurs et règlent la couleur de la lumière en fonction de l'humeur. Les jetons indiquent une humeur triste, heureuse ou en colère.

![Un jeton argenté est déposé dans une boîte et une lumière rouge s'affiche.](images/drop-switch.gif)

--- collapse ---
---
title: Voir à l'intérieur
---
--- code ---
---
language: python
filename: drop_switch.py
line_numbers: true
line_number_start: 
line_highlights: 
---
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
    elif colere.is_pressed: # Jaune
        print('EN COLERE!')
        led.color = (255,0,0) # Rouge
    elif triste.is_pressed: # CRecherche le jeton le plus court en dernier lieu
        print('triste et bleu...')
        led.color = (0,125,255) # Bleu

--- /code ---

--- /collapse ---

**Cadran d'humeur** Un potentiomètre est utilisé avec une seule LED RVB pour créer un cadran d'humeur. L'utilisateur peut tourner le cadran pour 'enregistrer' son humeur actuelle.

![On tourne un potentiomètre et une LED située derrière du papier change de couleur, éclairant ainsi une face de papier de la couleur choisie.](images/mood-dial.gif)

--- collapse ---
---
title: Voir à l'intérieur
---
--- code ---
---
language: python
filename: mood_dial.py
line_numbers: true
line_number_start: 
line_highlights: 
---

from picozero import RGBLED, Pot
from time import sleep

rgb = RGBLED(red=1, green=2, blue=3)
cadran = Pot(0)

def heureux(): rgb.color = (0, 255, 0) # Vert

def bien(): rgb.color = (75, 255, 0) # Jaune-vert

def ok(): rgb.color = (255, 150, 0) # Jaune

def incertain(): rgb.color = (255, 25, 0) # Orange

def malheureux(): rgb.color = (255, 0, 0) # Rouge


while True:
    humeur = cadran.value * 100 # transformer en un pourcentage
    print(humeur)
    if humeur < 20:
        heureux()
    elif humeur < 40:
        bien()
    elif humeur < 60:
        ok()
    elif humeur < 80:
        incertain()
    else:
        malheureux()
    sleep(0.1)

--- /code ---


--- /collapse ---

**Témoin de mise au point** Trois boutons et trois LED monochromes sont utilisés pour indiquer le type d'aide dont une personne a besoin dans un club. L'emoji 'Chut' signifie 'ne pas déranger', l'emoji 'confus' signifie qu'ils demandent de l'aide pour leur travail, et l'emoji 'smiley' signifie qu'ils travaillent avec plaisir.

![Une boîte avec trois emojis sur le devant. L'un est un emoji chut, l'autre est un emoji confus et l'autre est un visage souriant. Les boutons à côté d'eux sont enfoncés, ce qui allume une LED correspondante.](images/dnd-indicator.gif)

--- collapse ---
---
title: Voir à l'intérieur
---
--- code ---
---
language: python
filename: focus_indicator.py
line_numbers: true
line_number_start: 
line_highlights: 
---
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
        shh.on()
        confus.off()
        sourire.off()
    elif option == 1:
        shh.off()
        confus.on()
        sourire.off()    
    elif option == 2:
        shh.off()
        confus.off()
        sourire.on()   
    elif option == 3:
        shh.off()
        confus.off()
        sourire.off()

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
--- /code ---


--- /collapse ---

--- /no-print ---

--- print-only ---

## Trouve l'inspiration 💭

Explore ces exemples de projets pour obtenir plus d'idées .

**Lampe d'humeur** Un seul bouton est utilisé avec une seule LED RVB pour créer une lampe d'ambiance à l'aide d'un gobelet en carton et de papier calque. Chaque fois que l'on appuie sur le bouton, la couleur change. ![Une LED RVB unique est utilisée pour créer une lampe d'ambiance à l'aide d'un gobelet en carton et de papier calque.](images/mood-lamp.PNG)

**Cadran d'humeur** Un potentiomètre est utilisé avec une seule LED RVB pour créer un cadran d'humeur. L'utilisateur peut tourner le cadran pour 'enregistrer' son humeur actuelle. ![Un potentiomètre est utilisé avec une seule LED RVB pour créer un cadran d'humeur.](images/mood-dial.PNG)

**Témoin de mise au point** Trois boutons et trois LED monochromes sont utilisés pour indiquer le type d'aide dont une personne a besoin dans un club. L'emoji 'Chut' signifie 'ne pas déranger', l'emoji 'confus' signifie qu'ils demandent de l'aide pour leur travail, et l'emoji 'smiley' signifie qu'ils travaillent avec plaisir. ![Trois boutons et trois LED monochromes sont utilisés pour indiquer le type d'assistance dont une personne a besoin.](images/dnd-indicator.PNG)

--- /print-only ---

