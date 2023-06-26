## Verander je humeur

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Nu heb je een manier nodig voor de gebruiker om van humeur te veranderen met behulp van een knop- of potentiometerinvoer. 
</div>
<div>
![Een doos met drie emoji's aan de voorkant. Het ene is een stopteken, het andere is een 'handen omhoog'-teken en het andere is een 'OK'-teken. Knoppen ernaast worden ingedrukt, die de bijbehorende LED laten branden.](images/dnd-indicator.gif){:width="300px"}
</div>
</div>

--- task ---

**Zoek** de invoercomponenten die je wilt gebruiken voor je humeurmeter.

Je zou kunnen gebruiken:
+ Eén knop voor elke stemming
+ Een enkele knop om naar de volgende stemming te gaan
+ Twee bus–pin verbindingsdraden die je kunt aansluiten op een zelfgemaakte knop of schakelaar
+ Een potentiometer om je humeur te selecteren, afhankelijk van de positie van het instelwiel

Je hebt ook twee verbindingsdraden met stekkerbussen nodig voor elke knop of drie stekkerbussen voor een potentiometer.

--- /task ---

--- task ---

**Kies:** Sluit de gekozen invoercomponenten aan op de Raspberry Pi Pico.

\[[[single-button-wiring]]\] \[[[multiple-button-wiring\]]] \[[[potentiometer-wiring]]\] \[[[crafted-switch-button-wiring\]]] [[[multiple-crafted-switch-button-wiring]]]

**Tip:** als je onderdelen wilt gebruiken die je nog niet eerder hebt gebruikt, of als je nog meer onderdelen wilt bekabelen, bezoek dan onze [Inleiding tot Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico){:target="_blank"} gids.

--- /task ---

--- task ---

**Kies:** Importeer de gekozen invoercomponenten uit de picozero-bibliotheek en maak vervolgens variabelen aan voor de aangesloten pinnen.

**Tip:** je kunt meerdere imports combineren in één regel, bijvoorbeeld `from picozero import LED, button`.

\[[[single-button-pins]]\] \[[[multiple-button-pins\]]] \[[[single-switch-pins]]\] \[[[multiple-switches-pins\]]] [[[potentiometer-pin]]]

--- /task ---

--- task ---

**Kies:** Voeg code toe om je humeurfuncties aan te roepen op basis van de invoercomponent die je hebt gekozen.

--- collapse ---

---
title: Ga naar de volgende stemming wanneer er op een knop wordt gedrukt
---

Gebruik een `optie` variabele om de huidige stemming bij te houden, zodat je kunt beslissen welke functie je daarna wil aanroepen.

Zorg ervoor dat de functienamen overeenkomen met de humeurfuncties die je in de vorige stap hebt gedefinieerd.

--- code ---
---
language: python filename: mood_indicator.py
line_numbers: false
---
option = 0 # Store the current option

def choice(): # Call the next function and update the option global option if option == 0: energised() # Your first mood elif option == 1: calm()      # Your second mood elif option == 2: focused()   # Your third mood elif option == 3:    
rgb.off()

    # Move to the next option
    if option == 3:
        option = 0
    else:
        option = option + 1

button.when_pressed = choice # Call the choice function when the button is pressed

--- /code ---

--- /collapse ---

--- collapse ---

---
Title: Roep een andere functie op wanneer elke knop wordt ingedrukt
---

Je kunt meerdere knoppen hebben die elk een andere functie aanroepen wanneer ze worden ingedrukt.

Zorg ervoor dat je de functienamen van je project gebruikt, zonder haakjes.

--- code ---
---
language: python filename: mood_indicator.py
line_numbers: false
---

happy_button.when_pressed = happy sad_button.when_pressed = sad angry_button.when_pressed = angry

--- /code ---

--- /collapse ---

[[[potentiometer-function-value]]]

--- /task ---


--- task ---

**Test:** Voer je script uit en zorg ervoor dat je kunt schakelen tussen stemmingen.

--- /task ---

--- task ---

**Debug:** Mogelijk vind je enkele fouten in jouw project die je moet oplossen. Hier zijn enkele veelvoorkomende fouten.

\[[[debug-pico-code]]\] \[[[debug-pico-hardware\]]]

Als je een fout vindt die hier niet wordt vermeld. Kun je erachter komen hoe je het kunt oplossen?

We horen graag over je fouten en hoe je ze hebt opgelost. Gebruik de **Feedback verzenden** knop onderaan deze pagina en vertel ons of je een andere fout in je project hebt gevonden.

--- /task ---

