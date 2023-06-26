
--- question ---

---
legend: Question 2 sur 3
---

Tu essaies de faire clignoter une LED. En regardant ce code, que se passera-t-il lorsque tu appuieras sur le bouton ?

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

vert = LED(13)
bouton = Button(18)

def succes():
  vert.on()
  sleep(1)
  vert.off()

succes()

--- /code ---

--- choices ---

- (x) Rien ne se passera

  --- feedback ---

  C'est exact ! Le code crée une variable `bouton` mais il n'y a pas de code pour faire quoi que ce soit lorsque le bouton est enfoncé. Tu pourrais ajouter `button.when_pressed = success`.

  --- /feedback ---

- ( ) La lumière s'allume

  --- feedback ---

Réessaie. Relis le code et cherche où apparaît le `bouton`. Que fait-il ?

  --- /feedback ---

- ( ) La lumière s'éteint

  --- feedback ---

Réessaie. Relis le code et cherche où apparaît le `bouton`. Que fait-il ?

  --- /feedback ---

- ( ) La lumière s'allume et s'éteint à nouveau

  --- feedback ---

Réessaie. Le code *fait* allumer et éteindre la lumière, mais lis-le attentivement et cherche où le `bouton` apparaît. Que fait-il ?

  --- /feedback ---

--- /choices ---

--- /question ---
