## Concevoir ton appareil

<div style="display: flex; flex-wrap: wrap">
<div style="flex-basis: 200px; flex-grow: 1; margin-right: 15px;">
Comment ton appareil d'enregistrement d'humeur affichera-t-il les différentes humeurs ? Comment l'utilisateur sélectionnera-t-il son humeur ? 
</div>
<div>
![Un morceau de papier calque est enroulé autour d'un gobelet en carton. Une LED RVB se trouve à l'intérieur, qui éclaire le papier calque de différentes couleurs en fonction du nombre de fois que le bouton a été enfoncé.](images/mood-lamp.gif){:width="300px"}
</div>
</div>

--- task ---

**Choisir :** À qui s'adresse ton dispositif d'enregistrement d'humeur et comment sera-t-il utilisé ?

Ça pourrait être :
+ Pour communiquer ton humeur avec des adultes importants, des amis ou dans un club
+ Pour réfléchir à ta propre humeur et pour l'enregistrer pour toi-même
+ Pour aider quelqu'un qui a des difficultés à communiquer

--- /task ---

--- task ---

**Choisir :** Quelles humeurs ton appareil d'enregistrement d'humeur affichera-t-il ?

Tu pourrais utiliser :
+ Communiquer ton humeur : heureux, triste, en colère
+ Créer une ambiance : calme, concentrée, énergisée
+ Dans une session de club : je suis coincé, ne pas déranger, tout va bien
+ Commencer quelque chose de nouveau : appréhensif, excité, distrait

--- /task ---

--- task ---

**Choisir :** Comment ton appareil communiquera-t-il ton humeur à l'aide de motifs lumineux ?

--- collapse ---

---
title: Certaines couleurs ont-elles une signification pour toi?
---

+ Le rouge est une couleur populaire dans la culture chinoise, symbolisant la chance, la joie et le bonheur
+ Au théâtre, porter la couleur verte sur scène peut porter malheur
+ Selon la culture, le jaune, l'orange ou le rouge pourraient représenter le bonheur
+ Les couleurs plus vives sont associées à l'excitation
+ Le bleu et le vert sont associés au calme et à la relaxation

--- /collapse ---

Tu pourrais utiliser :
+ Différentes couleurs. Utiliseras-tu des couleurs associées aux humeurs ? Par exemple, le rouge pour la colère ou l'amour, le bleu pour le calme ou la tristesse.

Tu pourrais prendre des notes ou dessiner un croquis de ton plan.

--- /task ---

Le Raspberry Pi Pico a huit broches **GND**, donc lorsque tu utilises des fils de liaison, tu ne peux avoir que huit composants. Il n'y a qu'une seule broche **3V**, tu ne peux donc utiliser qu'un seul potentiomètre. Il y a aussi une limite à la quantité de courant que le Raspberry Pi Pico peut fournir, nous recommandons un maximum de deux LED RVB ou six LED monochromes.

Les combinaisons suggérées d'entrées et de sorties sont :
+ 3 boutons et 3 LED monochromes
+ 1 potentiomètre et 1 LED RVB à **cathode commune**
+ 1 bouton et 1 LED RVB à **cathode commune**
+ 4 boutons et 1 LED RVB à **cathode commune**

--- task ---

**Choisir :** Quelles LED utiliseras-tu avec ton appareil ?

Tu pourrais utiliser :
+ Des LED de différentes couleurs
+ Une ou plusieurs LED RVB

--- /task ---

--- task ---

**Choisir :** Quels composants d'entrée utiliseras-tu pour ton appareil ?

Tu pourrais utiliser :
+ Un ou plusieurs boutons
+ Un potentiomètre
+ Des boutons/commutateurs fabriqués qui établissent une connexion

--- /task ---

--- task ---

**Design :** À quoi ressemblera ton appareil d'enregistrement d'humeur ? Comment vas-tu connecter tes entrées et tes sorties ?

Tu pourrais :
+ T'inspirer des dessins de l'introduction
+ Intégrer tes composants dans une peluche
+ Transformer tes composants en un accessoire portable

**Astuce :** Tu n'as pas besoin de tout décider maintenant. Il est normal d'itérer sur ta conception lorsque tu commences à la fabriquer.

--- /task ---

