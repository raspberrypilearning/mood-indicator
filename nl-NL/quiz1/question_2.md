
--- question ---

---
legend: Vraag 2 van 3
---

Je probeert een LED te laten knipperen. Als je naar deze code kijkt, wat gebeurt er als je op de knop drukt?

--- code ---
---
language: python
filename: main.py
line_numbers: true
line_number_start: 1
line_highlights: 
---

from picozero import LED, Button
from time import sleep

groen = LED(13)
drukknop = Button(18)

def gelukt():
  groen.on()
  sleep(1)
  groen.off()

gelukt()

--- /code ---

--- choices ---

- (X) er zal niets gebeuren

  --- feedback ---

  Dat klopt! De code maakt een `drukknop` variabele, maar er is geen code om iets te doen wanneer de knop wordt ingedrukt. Je zou kunnen toevoegen `drukknop.when_pressed = gelukt`.

  --- /feedback ---

- ( ) het licht zal gaan branden

  --- feedback ---

Probeer het nog eens. Lees de code door en kijk waar de `drukknop` verschijnt. Wat doet het?

  --- /feedback ---

- ( ) het licht gaat uit

  --- feedback ---

Probeer het nog eens. Lees de code door en kijk waar de `drukknop` verschijnt. Wat doet het?

  --- /feedback ---

- ( ) het lampje gaat weer aan en uit

  --- feedback ---

Probeer het nog eens. De code *doet* het licht aan en uit laten gaan, maar lees het zorgvuldig door en kijk waar de `drukknop` verschijnt. Wat doet het?

  --- /feedback ---

--- /choices ---

--- /question ---
