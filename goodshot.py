import pgzrun

import random
'-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
TITLE = "Good shot"
WIDTH = 500
HEIGHT = 500

message = ""

#using Actor- built in object in pgzrun
#Actor is similar to the sprites in scratch. Actors are able to collide and move as well

beepbop = Actor("alien")
#beepbop.pos = (100, 100)
'-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------'
def draw():
    screen.clear()
    screen.fill(color = "black")
    beepbop.draw()
    #place_alien()

def place_alien():
    beepbop.x = random.randint(50, WIDTH-50)
    beepbop.y = random.randint(50, HEIGHT-50)

def on_mouse_down(pos):
    global message
    if beepbop.collidepoint(pos):
        message = "good shot!"
        place_alien()
    else:
        message = "you missed!"

place_alien()


pgzrun.go()