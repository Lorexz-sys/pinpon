from pygame import *



window = display.set_mode((1800,1075))
display.set_caption("pin-pon")
background = transform.scale(image.load("albinos-famosos5.jpg"),(1800,1075))
game = True 
finish = False
clock = time.Clock()

while game:
    for e in event.get():
        if e.type == QUIT:
            game = false
    display.update()
    window.blit(background,(0,0))