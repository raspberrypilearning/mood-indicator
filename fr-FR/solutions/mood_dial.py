from picozero import RGBLED, Pot
from time import sleep

rgb = RGBLED(red=1, green=2, blue=3)
cadran = Pot(0)

def heureux():
    rgb.color = (0, 255, 0) # Vert
    
def bien():
    rgb.color = (75, 255, 0) # Jaune-vert

def ok():
    rgb.color = (255, 150, 0) # Jaune
    
def incertain():
    rgb.color = (255, 25, 0) #Orange

def malheureux():
    rgb.color = (255, 0, 0) # Rouge
    

while True:
    humeur = cadran.percent
    print(humeur)
    if humeur < 20:
        heureux()
    elif humeur < 40:
        bien()
    elif humeur < 60:
        ok()
    elif humeur< 80:
        incertain()
    else:
        malheureux()
    sleep(0.1)
