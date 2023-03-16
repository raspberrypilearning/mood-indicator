## Codeer je sfeerlampjes

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Het is een goede gewoonte om je project geleidelijk te bouwen. In deze stap maak je verbinding en codeer je LED's om verschillende stemmingen weer te geven en te testen of dit werkt.
</div>
<div>
![Een potentiometer wordt gedraaid en een LED achter een papiertje verandert van kleur. Op het papier is een gezicht getekend.](images/mood-dial.gif){:width="300px"}
</div>
</div>

<p style="border-left: solid; border-width:10px; border-color: #0faeb0; background-color: aliceblue; padding: 10px;">
<span style="color: #0faeb0">Prototypen</span> houdt in dat je een concept maakt van wat je denkt dat je uiteindelijke project zou kunnen bereiken. Het doel van prototypen is om snel een vereenvoudigde versie van het eindproduct te maken, zodat je kunt testen of het een werkbare oplossing voor het probleem is.
</p>

Een prototype dat de aansluitingen en gecodeerde ontwerpkeuzes test zal eventuele bedrading- of codewijzigingen benadrukken die nodig zijn voordat de lichten in een apparaat worden ingebed.

--- task ---

**Kies:** Sluit je eenkleurige LED's of RGB LED aan op de Raspberry Pi Pico:

\[[[multiple-single-led-wiring]]\] \[[[rgb-wiring\]]]

**Tip:** als je de LED's nog niet hebt voorbereid en jezelf eraan moet herinneren hoe je LED's op weerstanden en verbindingsdraden kunt aansluiten, bezoek dan onze [Inleiding tot Raspberry Pi Pico](https://projects.raspberrypi.org/en/projects/introduction-to-the-pico){:target="_blank"} gids.

--- /task ---

--- task ---

**Kies:** Importeer LED of RGBLED uit de picozero-bibliotheek en stel vervolgens de pinnen in voor de aangesloten LED('s):

\[[[multiple-single-led-pins]]\] \[[[rgb-led-pins\]]]

--- /task ---

--- task ---

**Maken:** Maak functies voor elke stemming die je in je project wilt gebruiken.

**Kies:** Voeg code toe binnen de nieuwe functies om de LED in te stellen op het door jou gekozen ontwerp voor die stemming.

--- collapse ---

---
Title: Meerdere LED's met één kleur in- en uitschakelen
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

**Tip:** `knipperen`, `pulse` en `cyclus` stellen een lichtpatroon in dat kan worden onderbroken. Je kunt meteen weer op een knop drukken, zodat je met één druk op de knop kunt schakelen tussen lichteffecten.

--- collapse ---

---
Title: Knippert of pulseert meerdere LED's met één kleur
---

Gebruik blink of pulse om een LED in en uit te schakelen.

Een LED laten knipperen:

--- code ---
---
language: python filename: mood_indicator.py
line_numbers: false
---

def available(): # First mood red.off() # Turn off the red LED green.blink()


def do_not_disturb(): # First mood green.off() # Turn off the green LED red.pulse()

--- /code ---

**Tip:** je kunt in hetzelfde project enkele kleuren, knipperende effecten en pulseffecten mixen om de gewenste stemming te maken.

--- /collapse ---

--- collapse ---

---
Title: Schakel een RGB-LED met een specifieke kleur in
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
title: Een RGB-LED knipperen, pulseren of cyclus laten doorlopen
---

Gebruik `blink`, `pulse`, of `cyclus` om te wisselen tussen kleuren op een RGB LED.

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

**Tip:** Voeg opmerkingen toe aan je code naast de kleurwaarden zodat je weet welke kleuren je voor elke stemming hebt gemaakt.

--- /task ---

--- task ---

**Test:** Voeg aan het einde van je code, onder de definities van je stemmingsfunctie, code toe om je eerste functie aan te roepen.

Werk je nieuwe code bij om je stemmingsfuncties een voor een aan te roepen, en test elke code door je code uit te voeren.

--- collapse ---

---
Title: Roep een stemmingsfunctie op.
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

**Tip:** Zorg ervoor dat je nieuwe code niet inspringt.

--- /task ---

--- task ---

**Debug:** Mogelijk vind je enkele fouten in jouw project die je moet oplossen. Hier zijn enkele veelvoorkomende fouten.

\[[[debug-pico-code]]\] \[[[debug-pico-hardware\]]]

--- collapse ---

---
title: Mijn LED licht niet op als ik mijn stemmingsfunctie aanroep
---

Controleer of de pinnen in je code overeenkomen met de pinnen waarop je LED('s) zijn aangesloten.

--- /collapse ---

--- collapse ---

---
Title: Mijn RGB-LED geeft de verkeerde kleur aan
---

Controleer je code om er zeker van te zijn dat je kleurwaarden in de juiste volgorde staan. Gebruik de ['RGB kleur gids'](https://www.w3schools.com/colors/colors_rgb.asp){:target="_blank"} om te controleren of de code overeenkomt met de kleur die je verwacht.

--- /collapse ---

Als je een fout vindt die hier niet wordt vermeld. Kun je erachter komen hoe je het kunt oplossen?

We horen graag over je fouten en hoe je ze hebt opgelost. Gebruik de **Feedback verzenden** knop onderaan deze pagina en vertel ons of je een andere fout in je project hebt gevonden.

--- /task ---

