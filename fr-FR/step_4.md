## Changer ton humeur

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Maintenant, tu dois donner le moyen à l'utilisateur de changer d'humeur à l'aide d'un bouton ou d'une entrée de potentiomètre. 
</div>
<div>
![Une boîte avec trois emojis sur le devant. L'un est un panneau d'arrêt, l'autre est une main levée et l'autre est un panneau OK. Les boutons à côté d'eux sont enfoncés, ce qui allume la LED correspondante.](images/dnd-indicator.gif){:width="300px"}
</div>
</div>

--- task ---

**Recherche** les composants d'entrée que tu souhaites utiliser pour ton indicateur d'humeur.

Tu pourrais utiliser :
+ Un bouton pour chaque humeur
+ Un seul bouton pour passer à l'humeur suivante
+ Deux fils de liaison broche-prise que tu peux connecter à un bouton ou un interrupteur fabriqué
+ Un potentiomètre pour sélectionner l'humeur en fonction de la position du cadran

Tu auras également besoin de deux fils de liaison prise-prise pour chaque bouton ou de trois fils prise-prise pour un potentiomètre.

--- /task ---

--- task ---

**Choisir :** Connecte les composants d'entrée de ton choix au Raspberry Pi Pico.

[[[single-button-wiring]]]
[[[multiple-button-wiring]]]
[[[potentiometer-wiring]]]
[[[crafted-switch-button-wiring]]]
[[[multiple-crafted-switch-button-wiring]]]

**Astuce :** Si tu souhaites utiliser des composants que tu n'as pas utilisés auparavant, ou si tu as besoin d'en câbler d'autres, consulte notre guide [Présentation du Pico](https://projects.raspberrypi.org/fr-FR/projects/introduction-to-the-pico){:target="_blank"}.

--- /task ---

--- task ---

**Choisis :** Importe les composants d'entrée de ton choix à partir de la bibliothèque picozero, puis crée des variables pour les broches connectées.

**Astuce :** Tu peux combiner plusieurs importations sur une seule ligne, par exemple `from picozero import LED, Button`.

[[[single-button-pins]]]
[[[multiple-button-pins]]]
[[[single-switch-pins]]]
[[[multiple-switches-pins]]]
[[[potentiometer-pin]]]

--- /task ---

--- task ---

**Choisir :** Ajoute du code pour appeler tes fonctions d'humeur en fonction du composant d'entrée que tu as choisi.

--- collapse ---

---
title: Passe à l'humeur suivante lorsqu'un seul bouton est enfoncé
---

Utilise une variable `option` pour garder une trace de l'humeur actuelle afin que tu puisses décider quelle fonction appeler ensuite.

Assure-toi que les noms de fonction correspondent aux fonctions d'humeur que tu as définies à l'étape précédente .

--- code ---
---
language: python
filename: mood_indicator.py
line_numbers: false
---
option = 0 # Memorise l'option actuelle

def choix(): # Appelle la fonction suivante et mets a jour l'option
    global option
    if option == 0:
        energique() # Ta premiere humeur
    elif option == 1:
        calme()      # Ta deuxieme humeur
    elif option == 2:
        concentre()   # Ta troisieme humeur
    elif option == 3:    
        rgb.off()

    # Passer a l'option suivante
    if option == 3:
        option = 0
    else:
        option = option + 1
    
bouton.when_pressed = choix # Appelle la fonction de choix lorsque le bouton est enfonce

--- /code ---

--- /collapse ---

--- collapse ---

---
title: Appelle une fonction différente lorsque chaque bouton est enfoncé
---

Tu peux avoir plusieurs boutons qui appellent chacun une fonction différente lorsqu'ils sont enfoncés.

Assure-toi d'utiliser les noms de fonction de ton projet et n'utilise que le nom de la fonction, ne l'appelle pas en ajoutant des crochets.

--- code ---
---
language: python
filename: mood_indicator.py
line_numbers: false
---

bouton_heureux.when_pressed = heureux
bouton_triste.when_pressed = triste
bouton_colere.when_pressed = colere

--- /code ---

--- /collapse ---

[[[potentiometer-function-value]]]

--- /task ---


--- task ---

**Test :** Exécute ton script et assure-toi que tu peux passer d'une humeur à l'autre.

--- /task ---

--- task ---

**Débogage :** Il est possible que tu trouves des bogues dans ton projet que tu dois corriger. Voici quelques bogues assez courants.

[[[debug-pico-code]]]
[[[debug-pico-hardware]]]

Si tu trouves un bogue qui n'est pas répertorié ici. Peux-tu trouver comment le résoudre?

Nous aimons avoir des nouvelles de tes bogues et de la façon dont tu les as corrigés. Utilise le bouton **Envoyer des commentaires** en bas de cette page et dis-nous si tu as trouvé un bogue différent dans ton projet.

--- /task ---

