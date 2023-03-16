
--- question ---

---
legend: Vraag 2 van 3
---

Je probeert een LED te laten knipperen. Als je naar deze code kijkt, wat gebeurt er als je op de knop drukt?

--- code ---
---
language: python filename: main.py line_numbers: true line_number_start: 1
line_highlights:
---

from picozero import LED, Button from time import sleep

green = LED(13) button = Button(18)

def success(): green.on() sleep(1) green.off()

success()

--- /code ---

--- choices ---

- (X) er zal niets gebeuren

  --- feedback ---

  Dat klopt! De code maakt een `knop` variabele, maar er is geen code om iets te doen wanneer de knop wordt ingedrukt. Je zou kunnen toevoegen`button.when_pressed = success`.

  --- /feedback ---

- ( ) het licht zal gaan branden

  --- feedback ---

Probeer het nog eens. Lees de code door en kijk waar de `knop` verschijnt. Wat doet het?

  --- /feedback ---

- ( ) het licht gaat uit

  --- feedback ---

Probeer het nog eens. Lees de code door en kijk waar de `knop` verschijnt. Wat doet het?

  --- /feedback ---

- ( ) het lampje gaat weer aan en uit

  --- feedback ---

Probeer het nog eens. De code *doet* het licht aan en uit laten gaan, maar lees het zorgvuldig door en kijk waar de `knop` verschijnt. Wat doet het?

  --- /feedback ---

--- /choices ---

--- /question ---
