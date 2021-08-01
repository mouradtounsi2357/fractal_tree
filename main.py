#!/usr/bin/python3
#-------------------------------------------------------------------#
# MOURAD TOUNSI                                                     #
#-------------------------------------------------------------------#
import math, pygame, sys
from SLD import Slider

# initiation pygame ------------------------$
pygame.init()
display=pygame.display.set_mode((500,400))
pygame.display.set_caption("fractal tree")
clock=pygame.time.Clock()
fps=60

# classes ----------------------------------$
class Curseur():
    def __init__(self):
        self.pos=(250,250)
        self.angleP=math.pi/4
        self.angleO=math.pi/4
        self.size=80
        self.color=(200,200,200)

# fonctions --------------------------------$
def fractale(pos,size,angleP,angleO,color):
    if size <= 2:
        return 0
    
    pos1=(pos[0]+int(math.cos(angleP)*size),pos[1]+int(math.sin(angleP)*size))
    pygame.draw.line(display,color,pos,pos1,1)
    pos=pos1
    color=(int(color[0]/(12/11)),color[1],int(color[2]/(2)))

    fractale(pos,size/(3/2),angleP+angleO,angleO,color)
    fractale(pos,size/(3/2),angleP-angleO,angleO,color)
    
def draw_root():
    pygame.draw.line(display,(200,200,200),cr.pos,(250,400),1)

# setup & declaration ----------------------$
sld=Slider(display,(0,400-40))
cr=Curseur()
last_out=0.0
display.fill((0,0,50))
draw_root()

# main loop --------------------------------$
while 1:
    # logic --------------------------------$
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    sld.update()
    if last_out != sld.out:
        last_out=sld.out
        display.fill((0,0,50))

        cr.angleO=(sld.out*math.pi)
        cr.angleP=(sld.out*math.pi)-(math.pi/2)

        draw_root()
        fractale(cr.pos,cr.size,cr.angleP,cr.angleO,cr.color)
        fractale(cr.pos,cr.size,-cr.angleP-(math.pi),cr.angleO,cr.color)
        

    # draw ----------------------------------$
    sld.draw()

    # update screen -------------------------$
    pygame.display.flip()
    clock.tick(fps)

    

