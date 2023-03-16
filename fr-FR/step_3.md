## Coder tes lumières d'humeur

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
C'est une bonne pratique de construire ton projet progressivement. Dans cette étape, tu vas connecter et coder tes LEDs pour créer différentes humeurs et tester leur bon fonctionnement.
</div>
<div>
![Un potentiomètre est actionné et une LED derrière du papier change de couleur. Le papier a un visage dessiné dessus.](images/mood-dial.gif){:width="300px"}
</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">Le prototypage</span> consiste à faire une ébauche de ce que tu penses que ton projet final pourrait accomplir. L'objectif du prototypage est de créer une version simplifiée du produit final, pour te permettre de tester s'il s'agit d'une solution viable au problème.
</p>

Un prototype qui teste les connexions et les choix de conception codés mettra en évidence tous les changements de câblage ou de codage nécessaires avant que les lumières ne soient intégrées dans un appareil.

--- task ---

**Choisir :** Connecte tes LEDs monochromes ou LEDs RVB au Raspberry Pi Pico :

\[[[multiple-single-led-wiring]]\] \[[[rgb-wiring\]]]

**Astuce :** Si tu n'as pas encore préparé tes LEDs et que tu dois te rappeler comment connecter les LEDs aux résistances et aux fils de liaison, consulte notre guide [Introduction au Pico](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico){:target="_blank"}.

--- /task ---

--- task ---

**Choisir :** Importe LED ou RGBLED à partir de la librairie picozero puis définis les broches pour tes LED(s) connectées :

\[[[multiple-single-led-pins]]\] \[[[rgb-led-pins\]]]

--- /task ---

--- task ---

**Créer :** Crée des fonctions pour chaque ambiance que tu souhaites utiliser dans ton projet.

**Choisir :** Ajoute du code dans les nouvelles fonctions pour configurer la LED sur le motif de ton choix pour cette humeur.

--- collapse ---

---
title: Allumer et éteindre plusieurs LED monochromes
---

--- code ---
---
language: python filename: mood_indicator.py
line_numbers: false
---
def excited(): # Your first mood purple.on() # Turn on blue.off() # Turn off

def worried(): # Your second mood purple.off() # Turn off blue.on() # Turn on

--- /code ---

--- /collapse ---

**Astuce :** `clignotement`, `impulsions` et `cycle` définissent un motif lumineux qui peut être interrompu. Tu pourras à nouveau appuyer immédiatement sur un bouton pour pouvoir changer d'effet d'éclairage à l'aide d'un seul bouton.

--- collapse ---

---
title: Clignotement ou impulsion de plusieurs LED monochromes
---

Utilise le clignotement ou l'impulsion pour allumer et éteindre une LED.

Faire clignoter une LED :

--- code ---
---
language: python filename: mood_indicator.py
line_numbers: false
---

def available(): # First mood red.off() # Turn off the red LED green.blink()


def do_not_disturb(): # First mood green.off() # Turn off the green LED red.pulse()

--- /code ---

**Astuce :** Tu peux mélanger des effets de couleur unique, de clignotement et d'impulsion dans le même projet pour créer les humeurs que tu souhaites.

--- /collapse ---

--- collapse ---

---
title: Allumer une LED RVB d'une couleur spécifique
---

--- code ---
---
language: python filename: mood_indicator.py
line_numbers: false
---
def happy(): # Your first mood rgb.color = (0, 255, 0) # Your first colour

def sad(): # Your second mood rgb.color = (255, 0, 0) # Your second colour

--- /code ---

--- /collapse ---

--- collapse ---

---
title : Clignotement, impulsion ou cycle d'une LED RVB
---

Utilise `clignotement`, `impulsion`ou `cycle` pour passer d'une couleur à l'autre sur une LED RVB.

--- code ---
---
language: python filename: mood_indicator.py
line_numbers: false
---
def energise(): rgb.blink() # Red for 1 second, green for 1 second, blue for 1 second

def neutral(): rgb.pulse(fade_times=3) # Slow pulse

def relax(): rgb.cycle(fade_times=4) --- /code ---

--- /collapse ---

[[[generic-theory-simple-colours]]]

**Astuce :** Ajoute des commentaires à ton code à côté des valeurs de couleur afin de te souvenir des couleurs que tu as créées pour chaque ambiance.

--- /task ---

--- task ---

**Test :** À la fin de ton code, sous les définitions de tes fonctions d'humeur, ajoute du code pour appeler ta première fonction.

Mets ton nouveau code à jour pour appeler tes fonctions d'humeur une par une, en testant chacune d'entre elles en exécutant ton code.

--- collapse ---

---
title: Appeler une fonction
---

--- code ---
---
language: python filename: mood_indicator.py line_numbers: false line_number_start: 1
line_highlights: 7
---
def happy(): # Your first mood rgb.color = (0, 255, 0) # Your first colour

def sad(): # Your second mood rgb.color = (255, 0, 0) # Your second colour

happy() # Change this line to try each of your functions

--- /code ---

--- /collapse ---

**Astuce :** Assure-toi que ton nouveau code n'est pas indenté.

--- /task ---

--- task ---

**Débogage :** Il est possible que tu trouves des bogues dans ton projet que tu dois corriger. Voici quelques bogues assez courants.

\[[[debug-pico-code]]\] \[[[debug-pico-hardware\]]]

--- collapse ---

---
title: Ma LED ne s'allume pas lorsque j'appelle ma fonction d'humeur
---

Vérifie que les broches de ton code correspondent aux broches auxquelles tes LED(s) sont connectées.

--- /collapse ---

--- collapse ---

---
title : Ma LED RVB affiche la mauvaise couleur
---

Vérifie ton code pour t'assurer que tes valeurs de couleur sont dans le bon ordre. Utilise le ['Guide des couleurs RVB'](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} pour vérifier que ton code correspond à la couleur que tu attends.

--- /collapse ---

Si tu trouves un bogue qui n'est pas répertorié ici. Peux-tu trouver comment le réparer?

Nous aimons avoir des nouvelles de tes bogues et de la façon dont tu les as corrigés. Utilise le bouton **Envoyer des commentaires** en bas de cette page et dis-nous si tu as trouvé un bogue différent dans ton projet.

--- /task ---

