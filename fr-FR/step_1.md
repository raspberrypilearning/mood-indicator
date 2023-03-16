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

Tu peux acheter tout le matériel requis pour ce projet et les autres projets du parcours à partir de la [boutique en ligne Pimoroni.](https://shop.pimoroni.com/products/pico-intro-kit?variant=39893512945747){:target='_blank'}

Si tu as déjà un Raspberry Pi Pico, tu peux acheter les composants électroniques dont tu as besoin pour ce projet et les autres projets via [La boutique en ligne Kitronik.](https://kitronik.co.uk/products/5343-raspberry-pi-foundation-pico-pathway-pack)

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
language: python filename: mood_lamp.py line_numbers: true line_number_start: 1
line_highlights:
---
from picozero import RGBLED, Switch from time import sleep

rgb = RGBLED(red=1, green=2, blue=3) # Pin numbers switch = Switch(18)

option = 0

def calm(): rgb.color = (255, 255, 0) # Yellow

def focused(): rgb.color = (0, 215, 0) # Orange

def energised(): rgb.color = (63, 204, 208) # Green

def choice(): global option if option == 0: energised() elif option == 1: calm() elif option == 2: focused() elif option == 3:    
rgb.off()

    if option == 3:
        option = 0
    else:
        option = option + 1


switch.when_closed = choice --- /code ---

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
language: python filename: drop_switch.py line_numbers: true line_number_start:
line_highlights:
---
from time import sleep from picozero import Button, RGBLED


happy = Button(13) # Longest token angry = Button(14) # Medium token sad = Button(15) # Shortest token led = RGBLED(18, 17, 16)


while True: # Create a loop that checks for the different tokens if happy.is_pressed: # Look for the longest token first print('happy!') led.color = (255,255,0) # Yellow elif angry.is_pressed: # Check for the medium token next print('ANGRY!') led.color = (255,0,0) # Red elif sad.is_pressed: # Check for the shortest token last print('sad and blue...') led.color = (0,125,255) # Blue

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
language: python filename: mood_dial.py line_numbers: true line_number_start:
line_highlights:
---

from picozero import RGBLED, Pot from time import sleep

rgb = RGBLED(red=1, green=2, blue=3) dial = Pot(0)

def happy(): rgb.color = (0, 255, 0) # Green

def good(): rgb.color = (75, 255, 0) # Yellow-green

def okay(): rgb.color = (255, 150, 0) # Yellow

def unsure(): rgb.color = (255, 25, 0) # Orange

def unhappy(): rgb.color = (255, 0, 0) # Red


while True : humeur = cadran.value * 100 # transformer en un pourcentage print(humeur) if humeur < 20 : heureux() elif humeur < 40 : bon() elif humeur < 60 : ok( ) elif humeur < 80 : incertain() else : malheureux() sleep(0.1)

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
language: python filename: focus_indicator.py line_numbers: true line_number_start:
line_highlights:
---
from picozero import LED, Speaker, Button from time import sleep

eat = LED(13) drink = LED(8) play = LED(5)

speaker = Speaker(1)

choose = Button(18) confirm = Button(22)

option = 0 # Store the current option

def choice(): # Call the next function and update the option global option if option == 0: shh.on() confused.off() smile.off() elif option == 1: shh.off() confused.on() smile.off()    
elif option == 2: shh.off() confused.off() smile.on()   
elif option == 3: shh.off() confused.off() smile.off()

    if option == 3:
        option = 0
    else:
        option = option + 1

def sound_buzzer(): speaker.on() sleep(1) speaker.off()

choose.when_pressed = choice confirm.when_pressed = sound_buzzer --- /code ---


--- /collapse ---

--- /no-print ---

--- print-only ---

## Trouve l'inspiration 💭

Explore ces exemples de projets pour obtenir plus d'idées .

**Lampe d'humeur** Un seul bouton est utilisé avec une seule LED RVB pour créer une lampe d'ambiance à l'aide d'un gobelet en carton et de papier calque. Chaque fois que l'on appuie sur le bouton, la couleur change. ![Une LED RVB unique est utilisée pour créer une lampe d'ambiance à l'aide d'un gobelet en carton et de papier calque.](images/mood-lamp.PNG)

**Cadran d'humeur** Un potentiomètre est utilisé avec une seule LED RVB pour créer un cadran d'humeur. L'utilisateur peut tourner le cadran pour 'enregistrer' son humeur actuelle. ![Un potentiomètre est utilisé avec une seule LED RVB pour créer un cadran d'humeur.](images/mood-dial.PNG)

**Témoin de mise au point** Trois boutons et trois LED monochromes sont utilisés pour indiquer le type d'aide dont une personne a besoin dans un club. L'emoji 'Chut' signifie 'ne pas déranger', l'emoji 'confus' signifie qu'ils demandent de l'aide pour leur travail, et l'emoji 'smiley' signifie qu'ils travaillent avec plaisir. ![Trois boutons et trois LED monochromes sont utilisés pour indiquer le type d'assistance dont une personne a besoin.](images/dnd-indicator.PNG)

--- /print-only ---

